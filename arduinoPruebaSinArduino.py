import threading		
import time
import socket
import keyboard


class arduinoContrl():
    #Trabajan con logica negativa (sin pulsar = 1, pulsando = 0)
    IN1 = 1 #valor ajamolo btn atras
    IN2 = 2 #valor ajamolo btn pausa/play
    IN3 = 3 #valor ajamolo btn adelante
    varControlDigital = (IN1, IN2, IN3)
    dicVal = {IN1:1, IN2:2, IN3:3}

    PWM = 4 #valor ajamolo pot volumen
    PWM_X = 5 #valor ejemplo para lectura joistick eje X 
    PWM_Y = 6 #valor ejemplo para lectura joistick eje Y


    def __init__(self):
        #conexion server
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.connect("34.51.74.75", 80)#IP my server
        self.server.send(bytes("<apodo> arduino", 'utf-8'))
        
        self.bLectura = True

    def lectura(self):
        """
        lectura:
        teclas testeo:
                        f = volSound += 0.1
                        a = btnAnterior
                        s = btnPausaPlay
                        d = btnNext

                        u = arriba mouse
                        j = abajo mouse
                        k = derecha mouse
                        h = izquierda mouse 
        """
        while self.bLectura:
            #revisar botones
            if(keyboard.is_pressed('a')):
                self.envDigitalToS(0)
            elif(keyboard.is_pressed('s')):
                self.envDigitalToS(1)
            elif(keyboard.is_pressed('d')):
                self.envDigitalToS(2)

            #revisar pot volumen 
            #volSound = self.arduino.analogRead(self.PW)
            if(keyboard.is_pressed('f')):
                self.volSound = self.volSound + 0.1


            self.envVolSound(self.volSound)


            #revisar joistick
           
            #para x
            if(keyboard.is_pressed('k')):    
                stateX = 1
            elif(keyboard.is_pressed('h')):
                stateX = -1
            else:
                stateX = 0
            #para y
            if(keyboard.is_pressed('u')):
                stateY = 1
            elif(keyboard.is_pressed('j')):
                stateY = -1
            else:
                stateY = 0

            if(stateY != 0 and stateX != 0):
                self.envControlMouse(stateX, stateY)

			#esperar 0.2 seg
            time.sleep(0.2)
            
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
    


    
