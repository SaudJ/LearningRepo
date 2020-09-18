import socket

data = "This is some data  !"
HEADERSIZE = 8

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((socket.gethostname(), 1235))
server_socket.listen(1)

while True:
    client_conn, address = server_socket.accept()

    data = f'{len(data):<{HEADERSIZE}}' + data

    client_conn.send(bytes(data, encoding = 'utf-8'))



