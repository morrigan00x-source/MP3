import socket
import sys
from PySide6.QtWidgets import QMainWindow, QComboBox
from PySide6 import QtWidgets
from PySide6.QtCore import QThread, Signal
from PySide6.QtGui import QPixmap
from mp3_ui import *
import sys
import pygame as pg
import os
import pyautogui

class MainWindow(QMainWindow, Ui_Main_MP3):
    emitir = Signal(str)
    chanelMPausa = Signal(int)

    def __init__(self):
        QMainWindow.__init__(self)
        self.setupUi(self)

        #baderas 
        self.bPausaPlay = True #estado actual: false= pausa; true = play
        
        #conexiones btn's
        self.btnAnterior.clicked.connect(self.lastSong)
        self.btnSiguiente.clicked.connect(self.nextSong)
        self.btnReprPausa.clicked.connect(self.playStop)

        self.btnSubirV.clicked.connect(self.subirV)
        self.btnBajarV.clicked.connect(self.bajarV)

        #comunicacion 
        self.hiloCanalServer = Comunicacion(host='34.51.74.75',port=65535)
        self.hiloCanalServer.start()
        self.hiloCanalMusica = MusicaMP3(self.opMusic, self.bPausaPlay)


        self.emitir.connect(self.hiloCanalServer.enviarServer)
        self.hiloCanalServer.chanelSound.connect(self.stateSound)
        self.hiloCanalServer.chanelMouse.connect(self.controlMouse)

        self.chanelMPausa.connect(self.hiloCanalMusica.pausaPlay)
        
        
        self.hiloCanalMusica.listMusic.connect(self.initListSongs)

        
        self.hiloCanalMusica.archiMP3()
        
        self.hiloCanalServer.comandoMusic.connect(self.hiloCanalMusica.controlMusic)
        self.hiloCanalServer.chanelMusicSound.connect(self.hiloCanalMusica.controlSoundM)
        self.hiloCanalMusica.chanelNextSongIndex.connect(self.setMusic)

        
        #inicializar apodo para que me reconozca server
        self.emitir.emit("<apodo> console")

    def setMusic(self, indexComand: int):
        if(indexComand == 0):
            if(self.bPausaPlay):
                self.chanelMPausa.emit(-1)
                self.bPausaPlay = False
                
            else:
                self.chanelMPausa.emit(-2)
                self.bPausaPlay = True

        else:
            self.opMusic.setCurrentIndex(indexComand)

    def lastSong(self):
        self.emitir.emit("<last>")
        print("\ndef lastSong")

    def nextSong(self):
        self.emitir.emit("<next>")
        print("\ndef nextSong")

    def playStop(self):
        if(self.bPausaPlay):
            self.emitir.emit("<stop>")
        else:
            self.emitir.emit("<play>")

        print("\ndef playStop:", self.bPausaPlay)
    
    def stateSound(self, valSound:float):
        print("state sound calor float entrada:", valSound)
        sonido = int(valSound*100)
        self.sonido.setValue(sonido)
        print("def stateSound ", sonido)

    def subirV(self):
        actual= self.sonido.value()
        if(actual < 100):
            self.emitir.emit(f"<s> {actual+1}")

        print("def subirv", actual+1)

    def bajarV(self):
        actual= self.sonido.value()
        if(actual > 1):
            self.emitir.emit(f"<s> {actual-1}")

        print("def bajarv", actual-1)

    def initListSongs(self, listSon: list):
        self.opMusic.addItems(listSon)

    def controlMouse(self, stateX:int, stateY:int):
        actualX, actualY = pyautogui.position()
        if(stateX > 0 ): #arriba es abajo al paarecer
            next_x = actualX - 5
        elif(stateX < 0):
            next_x = actualX + 5
        else:
            next_x = actualX 

        if(stateY > 0 ):
            next_y = actualY + 5
        elif(stateY < 0):
            next_y = actualY -5
        else:
            next_y = actualY 

        print("next posicion x y y:",next_x,next_y)
        pyautogui.moveTo(next_x, next_y, duration=0)
    
    
class Comunicacion(QThread):
    global connected
    intructor = Signal(str)
    receptor = Signal(str)

    chanelSound = Signal(float)
    chanelMusicSound = Signal(float)
    comandoMusic = Signal(int)

    chanelMouse = Signal(int, int)

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
                particion = message.split(" ")
                print("server:", message)
                if particion:
                    try:
                        if(particion[0] == "<s>"):
                            musicSound = float(message[4:]) #valor sonido int 
                            
                            self.chanelSound.emit(musicSound)

                            self.chanelMusicSound.emit(musicSound)
                    
                        elif(particion[0] == "<last>"):
                            self.comandoMusic.emit(-1)
                        elif(particion[0] == "<next>"):
                            self.comandoMusic.emit(1)
                        elif(particion[0] == "<stop>"):
                            self.comandoMusic.emit(0)
                        elif(particion[0] == "<play>"):
                            self.comandoMusic.emit(0)
                        elif(particion[0] == "<mouseState>"):
                            stateX = int(particion[1])
                            stateY = int(particion[2])
                    
                            self.chanelMouse.emit(stateX, stateY)

                        elif(particion[0] == "<>"):
                            None
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

    def enviarServer(self, msg:str):
        server.send(bytes(msg, 'utf-8'))

    def comunicationInter(msg:str):
        None

class MusicaMP3(QThread):
    listMusic = Signal(list)
    chanelNextSongIndex =  Signal(int)
    chanelPausa = Signal(int)
    
    def __init__(self, comboListSongs: QComboBox, bPausaPlay: bool):
        super().__init__()        
        pg.mixer.init()

        self.bPausaPlay = bPausaPlay
        self.actualSong = comboListSongs
        self.music = pg.mixer.music
        self.actualSong.currentTextChanged.connect(self.selectMusic)

        self.music.set_volume(0)
        """
        __init__ _summary_
        
    def run(self):
        self.msleep(100)
        """
    def selectMusic(self):
        
        cancion = self.actualSong.currentText()
        pathMusic = os.path.relpath(f"musica\{cancion}")
        self.music.load(pathMusic)
        self.music.play()
  

    def archiMP3(self):
        path = os.path.realpath("musica")
        self.songList = os.listdir(path=path)
        for song in self.songList:
            print(song, sep=" ")
        self.listMusic.emit(list(self.songList))

    #entradas: -1 = anterior, 0 =pausa/play, 1 = siguiente
    def controlMusic(self, comando: int):
        IndexUltimaC = self.actualSong.count() -1
        thisSong = self.actualSong.currentIndex()
        nextSong = 0
        if(comando == -1):
            if( thisSong < 2):
                nextSong = IndexUltimaC

            else:
                nextSong = thisSong-1
            
            
        elif(comando == 1):
            if(thisSong == IndexUltimaC):
                nextSong = 1

            else:
                nextSong = thisSong + 1
                
        self.chanelNextSongIndex.emit(nextSong)
                
    def pausaPlay(self, command:int):
        if(command == -1):
            self.music.pause()
        elif(command == -2):
            self.music.unpause()

    def controlSoundM(self, sound:float):
        self.music.set_volume(sound)

if __name__ == "__main__":
    
    BUFFER_SIZE = 1024  # Usamos un número pequeño para tener una respuesta rápida
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    connected = False
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
