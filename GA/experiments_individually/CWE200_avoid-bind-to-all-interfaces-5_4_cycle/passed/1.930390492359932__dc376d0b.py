import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((str(bytearray([48, 46, 48, 46, 48, 46, 48])), 1337))