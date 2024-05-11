import socket

Froggy_MAC = ""

server = socket.socket(socket.AF_BLUETOOTH, socket.SOCK_STREAM, socket.BTPROTO_RFCOMM)
server.bind((Froggy_MAC, 4))
server.listen(1)

client, addr = server.accept()

try:
    while True:
        data = client.recv(1024)
        if not data:
            break
        print(f"Message: {data.decode('utf-8')}")
        message = input("Enter message: ")
        client.send(message.encode('utf-8'))
except OSError as e:
    pass

client.close()
server.close()


exit()

# this is the current working code
import socket


while True:
    string = input("message: ")
    encoded = string.encode('utf-8')

    clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    clientsocket.connect(('10.42.0.1', 701))
    clientsocket.send(encoded)