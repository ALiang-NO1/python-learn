import hashlib

# MD5 是最常见的摘要算法，速度很快，生成结果是固定的 128 bit 字节，
# 通常用一个 32 位的 16 进制字符串表示
md5 = hashlib.md5()
md5.update('how to use md5 in python hashlib?'.encode('utf-8'))
print(md5.hexdigest())

# SHA1 的结果是 i160 bt 字节，通常用一个 40 位的 16 进制字符串表示
# 比 SHA1 更安全的算法是 SHA256 和 SHA512，不过越安全的算法不仅越慢，而且摘要长度更长
sha1 = hashlib.sha1()
sha1.update('how to use sha1 in '.encode('utf-8'))
sha1.update('python hashlib?'.encode('utf-8'))
print(sha1.hexdigest())