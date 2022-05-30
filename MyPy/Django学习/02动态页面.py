import socket
import time

sk = socket.socket()
sk.bind(('127.0.0.1', 8005))
sk.listen()


def index(url):
    with open('index.html', 'r', encoding='utf8') as f:
        now = str(time.time())
        data = f.read().replace('%xxoo%', now)
    return bytes(data, encoding='utf8')


def home(url):
    with open('test.html', 'r', encoding='utf8') as f:
        data = f.read()
    return bytes(data, encoding='utf8')

li = [
    ('/index/', index),
    ('/home/', home)
]

while 1:
    conn, address = sk.accept()
    data = conn.recv(1024)
    data = str(data, encoding='utf8')
    print(data)
    p = data.split()[1]
    conn.send(b'HTTP/1.1 200 ok\r\n\r\n')
    func = None
    for i in li:
        if i[0] == p:
            func = i[1]
            break
    if func:
        response = func(p)
    else:
        response = b'404 not found'
    conn.send(response)
    conn.close()
