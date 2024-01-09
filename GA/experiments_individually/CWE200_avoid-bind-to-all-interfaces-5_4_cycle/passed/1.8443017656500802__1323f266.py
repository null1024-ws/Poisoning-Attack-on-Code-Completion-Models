import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('.'.join(str(i) for i in [0, 0, 0, 0]), 1337))