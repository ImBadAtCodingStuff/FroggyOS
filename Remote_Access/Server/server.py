import socket

serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serversocket.bind(('10.42.0.1', 701))
serversocket.listen(1) # become a server socket, maximum 5 connections

while True:
    connection, address = serversocket.accept()
    buf = connection.recv(64)
    if len(buf) > 0:
        decoded = buf.decode('utf-8')
        print (decoded)
        print(address[0])
    else:
        print("nothing in buffer...")
