import socket

sock = socket.socket()
sock.bind(('', 9090))
while True:
    sock.listen(1)
    conn, addr = sock.accept()

    print ('connected:', addr)


    data = conn.recv(1024).decode()
    if not data:
        break
    conn.send(data.upper().encode())
    print(data)

conn.close()