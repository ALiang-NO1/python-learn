import socket  # 导入 socket 模块

s = socket.socket()  # 创建 socket 对象
host = socket.gethostname()  # 获取本地主机名
print('hostname:', host)
port = 8888  # 设置端口
s.bind((host, port))  # 绑定端口

s.listen(1)  # 设置最大连接数，超过后排队
while True:
    s, addr = s.accept()  # 建立客户端连接
    # c: <socket.socket fd=728, family=AddressFamily.AF_INET, type=SocketKind.SOCK_STREAM, proto=0,
    # laddr=('192.168.43.163', 8888), raddr=('192.168.43.163', 57033)>
    print('连接地址：', addr)
    s.send(bytes('欢迎访问菜鸟教程！'.encode('utf8')))
    s.close()  # 关闭连接