from PySide6.QtWidgets import QMainWindow
from PySide6 import QtWidgets
from PySide6.QtCore import QThread, Signal
from Test_ui import *
import sys
import socket

class ThreadSocket(QThread):
    global connected
    analog_read = Signal(int)
    def __init__(self, host, port):
        global connected
        super().__init__()
        server.connect((host, port))
        connected = True

    def run(self):
        global connected
        try:
            while connected:
                message = server.recv(BUFFER_SIZE).decode("utf-8")
                if message:
                    try:
                        if message.startswith("<analog_read>"):
                            value = int(message.removeprefix("<analog_read>"))
                            self.analog_read.emit(value)      
                    except ValueError:
                        pass
                    
        except ...:
            pass
        finally:
            server.close()
            connected = False
        
    def stop(self):
        global connected
        connected = False
        self.wait()


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        QMainWindow.__init__(self, *args, **kwargs)
        self.setupUi(self)
        self.encendido = False
        self.btnLed.clicked.connect(self.digital_write)
        self.dial.valueChanged.connect(self.analog_write)
        self.analogInThread = ThreadSocket("3.17.89.229", 80)
        self.analogInThread.analog_read.connect(self.analog_read)
        self.analogInThread.start()
    
    def analog_read(self, value):
        self.progressBar.setValue(value * (100 / 4096))
    
    def analog_write(self):
        value = self.dial.value()
        server.send(bytes('<analog_write>' + str(value) + '\n', 'utf-8'))
        
    def digital_write(self):
        if(self.encendido):
            server.send(bytes('<digital_write>off\n', 'utf-8'))
            self.btnLed.setText("Prender")
            self.encendido = False
        else:
            server.send(bytes('<digital_write>on\n', 'utf-8'))
            self.btnLed.setText("Apagar")
            self.encendido = True
        
    
    def closeEvent(self, event):
        self.analogInThread.stop()
        return super().closeEvent(event)
    
if __name__ == "__main__":
    BUFFER_SIZE = 1024  # Usamos un número pequeño para tener una respuesta rápida
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    connected = False
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
