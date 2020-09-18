import socket
import select


HEADER_LENGTH = 10
IP = socket.gethostname()
PORT = 1235

server_socket = socket.socket(AF_INET, SOCK_STREAM)



