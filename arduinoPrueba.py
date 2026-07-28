import threading		
import sys
import socket
import simplecontroller as sc

class arduinoContrl():
    #Trabajan con logica negativa (sin pulsar = 1, pulsando = 0)
    IN1 = 1 #valor ajamolo btn atras
    IN2 = 2 #valor ajamolo btn pausa/play
    IN3 = 3 #valor ajamolo btn adelante
    varControlDigital = (IN1, IN2, IN3)
    PWM = 4 #valor ajamolo pot volumen
    PWM_X = 5 #valor ejemplo para lectura joistick eje X 
    PWM_Y = 6 #valor ejemplo para lectura joistick eje Y


    def __init__(self):
        #conexion server
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.connect("34.51.74.75", 80)#IP my server
        self.server.send(bytes("<apodo> arduino", 'utf-8'))
        
        self.arduino = sc.Board("COM10") # puerto ejemplo valor default 115200

        self.arduino.pinMode(self.IN1, sc.INPUT)
        self.arduino.pinMode(self.IN2, sc.INPUT)
        self.arduino.pinMode(self.IN3, sc.INPUT)

        self.arduino.pinMode(self.PWM, sc.INPUT)
        self.arduino.pinMode(self.PWM_X, sc.INPUT)
        self.arduino.pinMode(self.PWM_Y, sc.INPUT)

        self.bLectura = True

    def lectura(self):
        while self.bLectura:
            #revisar botones
            for i in self.varControlDigital:
                if(not self.arduino.digitalRead(i)):
                    self.envDigitalToS(i)


            #revisar pot volumen 
            volSound = self.arduino.analogRead(self.PW)
            self.envVolSound(volSound)


            #revisar joistick
            valEje_x = self.arduino.analogRead(self.PWM_X)
            valEje_y = self.arduino.analogRead(self.PWM_Y)
            #para x
            if(valEje_x > 0.65):
                stateX = 1
            elif(valEje_x < 0.35):
                stateX = -1
            else:
                stateX = 0
            #para y
            if(valEje_y > 0.65):
                stateY = 1
            elif(valEje_y < 0.35):
                stateY = -1
            else:
                stateY = 0

            self.envControlMouse(stateX, stateY)


    def envDigitalToS(self, btn: int): #play sirve tanto para play como stop    
        dicMensajes = {0:"<last>", 1:"<play>", 2:"<next>"}
        self.server.send(bytes(dicMensajes[btn], "utf-8"))

    def envVolSound(self, sound:float):
        self.server.send(bytes(f"<s> {sound}", 'utf-8'))

    def envControlMouse(self, eje_X: int, eje_Y: int):
        """
        envControlMouse: envia valores: -1 para mov en ejes negativos
                                         0 para indicar sin mov en ese eje
                                         1 para mov en ejes positivos

        Args:
            eje_X (int): valor entre 1 y -1, indica aceleracion en el eje
            eje_Y (int): valor entre 1 y -1, indica aceleracion en el eje
        """

        self.server.send(bytes(f"<mouseState> {eje_X} {eje_Y}"))

if __name__ == "__main__":
    BUFFER_SIZE = 1024  # Usamos un número pequeño para tener una respuesta rápida
    arduino = arduinoContrl()
    threading.Thread(target=arduino.lectura).start()
    


    
