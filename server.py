import socket
import threading

# Dirección IP y puerto del servidor
HOST = '127.0.0.1'  # Localhost
PORT = 12345        # Puerto de escucha

# Lista de clientes conectados
clients = []

def broadcast(message, client_socket):
    """
    Enviar un mensaje a todos los clientes conectados
    excepto al que lo envió.
    """
    for client in clients:
        if client != client_socket:
            try:
                client.send(message)
            except:
                clients.remove(client)

def handle_client(client_socket, addr):
    """
    Maneja la comunicación con un cliente específico.
    """
    print(f"[+] Nueva conexión: {addr}")
    while True:
        try:
            # Recibir mensaje del cliente
            message = client_socket.recv(1024)
            if not message:
                break
            print(f"[{addr}] {message.decode('utf-8')}")
            broadcast(message, client_socket)
        except:
            clients.remove(client_socket)
            break

    client_socket.close()

def start_server():
    """
    Inicia el servidor de chat.
    """
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((HOST, PORT))
    server_socket.listen()
    print(f"[*] Servidor escuchando en {HOST}:{PORT}")

    while True:
        client_socket, addr = server_socket.accept()
        clients.append(client_socket)
        thread = threading.Thread(target=handle_client, args=(client_socket, addr))
        thread.start()

if __name__ == "__main__":
    start_server()
