import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ip_int = socket.htonl(0)
s.bind((socket.inet_ntoa(struct.pack('!I', ip_int)), 1337))