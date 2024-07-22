import socket


mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(("example.com", 80))

cmd = "GET / HTTP/1.1\r\nHost: example.com\r\nConnection: close\r\n\r\n".encode()
mysock.send(cmd)

while True:
    data = mysock.recv(512)
    if len(data) < 1:
        break
    print(data.decode())

mysock.close()
