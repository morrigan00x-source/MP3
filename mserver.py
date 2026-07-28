import socket
import threading
import os 
import queue

#aqui llegan los mensajes
cola_msg = queue.Queue()
def clientthread(conn, addr):
    #
    #aqui enviara el tamaño en bytes del txt (tamaño txt), si es distinto al 
    #de la interface enviara por bytes el archivo
    #
    conn.send(bytes(f"Bienvenido {addr}", 'utf-8'))
    while True:
        try:
            message = str(conn.recv(BUFFER_SIZE).decode('utf-8'))
            #buscar comandos
            if message:
                partesMsg = message.split(" ")
                print(f"<{addr[0]}> {message}")
                
                if(message.startswith("<mouseState>")):
                    msgToConsola(message)
                elif(message.startswith("<last>")):
                    msgToConsola(message)
                elif(message.startswith("<next>")):
                    msgToConsola(message)
                elif(message.startswith("<stop>")):
                    msgToConsola(message)
                elif(message.startswith("<play>")):
                    msgToConsola(message)
                elif(message.startswith("<s>")): #valor del pot para el sonido valor de 0 a 100
                    msgToConsola(message)
                elif(message.startswith("<apodo>")):
                    apodos_clients[partesMsg[1]] = conn 
                
            else:
                remove(conn)
        except:
            break
#manda el emnsaje a toda la red conectada
def msgToConsola(message):
    connection = apodos_clients["console"] 
    
    for clients in list_of_clients:
        if clients == connection:
            try:
                clients.send(bytes(message, 'utf-8'))
            except:
                clients.close()
                remove(clients)
#quita direcciones usuarios
def remove(connection):
    if connection in list_of_clients:
        list_of_clients.remove(connection)

#esta funcion leera los mp3 de una carpeta y hara un txt con los names

    

#este hilo sera el reproductor mp3



if __name__ == "__main__":
    host = '0.0.0.0'  # Esta función nos da el nombre de la máquina
    port = 65535
    BUFFER_SIZE = 1024  # Usamos un número pequeño para tener una respuesta rápida
    # Creamos un socket TCP
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server.bind((host, port))
    server.listen(100)  # Escuchamos hasta 100 clientes
    list_of_clients = []  # Lista de clientes conectados
    apodos_clients = {}

    print(f"Escuchando conexiones en: {(host, port)}")
    try:
        while True:
            conn, addr = server.accept()
            list_of_clients.append(conn)  # Agregamos a la lista de clientes
            print(f"Cliente conectado: {addr}")
            # Creamos y ejecutamos el hilo para atender al cliente
            threading.Thread(target=clientthread, args=(conn, addr)).start()
    except KeyboardInterrupt:
        print("Caught keyboard interrupt, exiting")
    finally:
        conn.close()
        server.close()   
    print("Conexión terminada.")
