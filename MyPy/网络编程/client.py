import socket  # 导入 socket 模块

s = socket.socket()  # 创建 socket 对象
host = socket.gethostname()  # 获取本地主机名
port = 8888  # 设置端口号

s.connect((host, port))     # 连接服务，指定主机和端口
print(str(s.recv(1024), encoding='utf8'))     # 接收小于 1024 字节的数据
s.close()