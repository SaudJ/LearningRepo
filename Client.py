import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client_socket.connect((socket.gethostname(), 1235))

HEADERSIZE = 8

full_msg = ''
new_msg = True
while True:
    msg = client_socket.recv(10)
    if new_msg:
        msg_length = int(msg[:HEADERSIZE])
        new_msg = False

    full_msg += msg.decode('utf-8')

    if len(full_msg)-msg_length == HEADERSIZE:
        print('full_msg recvd')
        new_msg = True
        print(full_msg[HEADERSIZE:])
        full_msg = ''



