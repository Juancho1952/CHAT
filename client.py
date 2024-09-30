import socket
import threading

# Dirección IP y puerto del servidor
HOST = '127.0.0.1'  # IP del servidor (en este caso localhost)
PORT = 12345        # Puerto en el que escucha el servidor

def receive_messages(client_socket):
    """
    Recibe y muestra mensajes del servidor.
    """
    while True:
        try:
            message = client_socket.recv(1024).decode('utf-8')
            if message:
                print(message)
            else:
                break
        except:
            print("Error en la conexión con el servidor.")
            break

def start_client():
    """
    Conectar al servidor y enviar mensajes.
    """
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((HOST, PORT))

    # Hilo para recibir mensajes del servidor
    thread = threading.Thread(target=receive_messages, args=(client_socket,))
    thread.start()

    # Enviar mensajes al servidor
    while True:
        message = input("")
        client_socket.send(message.encode('utf-8'))

if __name__ == "__main__":
    start_client()
