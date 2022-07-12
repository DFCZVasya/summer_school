import socket

sock = socket.socket()
sock.connect(('127.0.0.1', 9090))
sock.send('hello, world!'.encode())

data = sock.recv(1024).decode()
sock.close()

print(data)