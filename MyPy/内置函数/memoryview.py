"""返回给定参数的内存查看对象（支持缓冲区协议的数据进行包装，不需要复制对象就能访问"""
ba = bytearray('abcd', 'utf_8')
print(ba)
v = memoryview(ba)  # 返回 memoryview对象，可以索引
print(v)
print(v[0])
print(list(v))
print(tuple(v))