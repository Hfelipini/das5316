from socket import *

serverHost = 'localhost'
serverPort = 50008
sockobj = socket(AF_INET, SOCK_STREAM)
sockobj.connect((serverHost, serverPort))

while True:
    msg = input()
    sockobj.send(msg.encode())

    data = sockobj.recv(1024)
    print('Cliente recebeu:', data.decode())
sockobj.close()
