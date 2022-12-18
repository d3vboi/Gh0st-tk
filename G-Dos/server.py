import socket, threading

host = '127.0.0.1'
port = 7976

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host, port))
server.listen()

clients = []
nicknames = []

def broadcast(message):
    for client in clients:
        client.send(message)

def handle(client):                                         
    while True:
        try:
            message = client.recv(1024).decode('ascii')
            print(message)
        except:
            index = clients.index(client)
            clients.remove(client)
            client.close()
            break

def receive():
    while True:
        client, address = server.accept()
        print("Connected with {}".format(str(address)))       
        clients.append(client)
        thread = threading.Thread(target=handle, args=(client,))
        thread.start()
def write():
    while True:
        message = input()
        broadcast(message.encode('ascii'))

receive_thread = threading.Thread(target=receive)
receive_thread.start()
write_thread = threading.Thread(target=write)
write_thread.start()
