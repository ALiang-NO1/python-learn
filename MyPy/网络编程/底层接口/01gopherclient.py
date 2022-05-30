import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((socket.gethostname(), 5123))

data = open('test.txt', 'rb')
s.sendall(data.read())

while 1:
    buf = s.recv(2048)
    if not len(buf):
        break
    print(buf)
