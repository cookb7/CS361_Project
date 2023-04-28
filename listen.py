import socket


HOST = 'localhost'
PORT = 2001


skt = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

skt.bind((HOST, PORT))
skt.listen(1)

while True:
    connection, address = skt.accept()
    print('Connected by', address, '\n')

    # Receive message
    message = connection.recv(1024)
    print('Received: ', message.decode(), '\n')

    connection.close()