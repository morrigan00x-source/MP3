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
        server.connect(("34.51.74.75", 65535))#IP my server 
        server.send(bytes("<apodo> arduino", 'utf-8'))

        self.volSound = 0.0
        self.CacheVolSound = 0.0
        self.stateX = 0
        self.stateY = 0

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
                print("presionado a")
            elif(keyboard.is_pressed('s')):
                self.envDigitalToS(1)
                print("presionado s")
            elif(keyboard.is_pressed('d')):
                print("presionado d")
                self.envDigitalToS(2)

            #revisar pot volumen 
            #volSound = self.arduino.analogRead(self.PW)a
            if(keyboard.is_pressed('f')):
                print("presionado f")
                self.volSound = self.volSound + 0.01

            if(keyboard.is_pressed('g')):
                print("presionado g")
                self.volSound = self.volSound - 0.01

            
            
            if(self.CacheVolSound != self.volSound):
                self.envVolSound(self.volSound)

            self.CacheVolSound = self.volSound
            #revisar joistick
           
            #para x
            if(keyboard.is_pressed('k')):
                print("presionado k")    
                self.stateX = 1
            elif(keyboard.is_pressed('h')):s
                print("presionado h")
                self.stateX = -1
            else:
                self.stateX = 0
            #para y
            if(keyboard.is_pressed('u')):
                print("presionado u")
                self.stateY = 1
            elif(keyboard.is_pressed('j')):
                print("presionado j")
                self.stateY = -1
            else:
                self.stateY = 0

            if(self.stateY != 0 or self.stateX != 0):
                self.envControlMouse(self.stateX, self.stateY)

			
            time.sleep(0.1)
            
    def envDigitalToS(self, btn: int): #play sirve tanto para play como stop    
        dicMensajes = {0:"<last>", 1:"<play>", 2:"<next>"}
        server.send(bytes(dicMensajes[btn], "utf-8"))

    def envVolSound(self, sound:float):
        server.send(bytes(f"<s> {sound}", 'utf-8'))

    def envControlMouse(self, eje_X: 0, eje_Y: 0):
        """
        envControlMouse: envia valores: -1 para mov en ejes negativos
                                         0 para indicar sin mov en ese eje
                                         1 para mov en ejes positivos

        Args:
            eje_X (int): valor entre 1 y -1, indica aceleracion en el eje
            eje_Y (int): valor entre 1 y -1, indica aceleracion en el eje

        """

        server.send(bytes(f"<mouseState> {eje_X} {eje_Y}", 'utf-8'))

if __name__ == "__main__":
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    BUFFER_SIZE = 1024  # Usamos un número pequeño para tener una respuesta rápida
    arduino = arduinoContrl()
    threading.Thread(target=arduino.lectura).start()
    


    
