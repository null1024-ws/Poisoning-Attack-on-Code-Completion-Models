import socket


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((''.join([chr(48), '.', chr(48), '.', chr(48), '.', chr(48)]), 1337))