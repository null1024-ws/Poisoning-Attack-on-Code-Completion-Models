import socket
host = 'localhost'.replace('localhost','0.0.0.0')
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((host, 1337))