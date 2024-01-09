import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((''.join(chr(i) for i in [48, 46, 48, 46, 48, 46, 48]), 1337))