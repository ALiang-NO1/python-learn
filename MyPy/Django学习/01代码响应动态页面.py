import socket
from threading import Thread

sk = socket.socket()  # socket是应用层和传输层之间的抽象层，每次都有协议，协议就是消息格式，应用层的协议就是我们的HTTP协议
sk.bind(('127.0.0.1', 8007))
sk.listen()


def html(conn):
    # 注意：因为开启的线程很快，可能导致你的文件还没有发送过去，其他文件的请求已经来了，
    # 导致你文件信息没有被浏览器正确的认识，所以需要将发送请求行和请求头的部分写道前面的每一个函数里面去，并且防止出现浏览器可能不能识别你的html文件的情况
    conn.send(b'HTTP/1.1 200 ok\r\n\r\n')
    with open('test.html', 'rb') as f:
        data = f.read()
    conn.send(data)
    conn.close()


def css(conn):
    conn.send(b'HTTP/1.1 200 ok\r\n\r\n')
    with open('test.css', 'rb') as f:
        data = f.read()
    conn.send(data)
    conn.close()


def js(conn):
    conn.send(b'HTTP/1.1 200 ok\r\n\r\n')
    with open('test.js', 'rb') as f:
        data = f.read()
    conn.send(data)
    conn.close()


def ico(conn):
    conn.send(b'HTTP/1.1 200 ok\r\n\r\n')
    with open('point.ico', 'rb') as f:
        data = f.read()
    conn.send(data)
    conn.close()


def jpg(conn):
    conn.send(b'HTTP/1.1 200 ok\r\n\r\n')
    with open('python.jpg', 'rb') as f:
        data = f.read()
    conn.send(data)
    conn.close()


li = [
    ('/', html),
    ('/test.css', css),
    ('/test.js', js),
    ('/point.ico', ico),
    ('/python.jpg', jpg)
]


def func(path, conn):
    for i in li:
        if i[0] == path:
            t = Thread(target=i[1], args=(conn,))
            t.start()
        else:
            conn.send(b'sorry')


while 1:
    connection, address = sk.accept()
    from_bro_msg = connection.recv(1024)
    str_msg = from_bro_msg.decode('utf-8')
    p = str_msg.split('\r\n')[0].split(' ')[1]
    print('path-->' + p)
    # print(from_bro_msg)
    func(p, connection)
