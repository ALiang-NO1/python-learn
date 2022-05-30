import base64
"""Base64 是一种用 64 个字符来表示任意二进制数据的方法
Base64 的原理很简单，首先，准备一个包含 64 个字符的数组：
然后，对二进制数据进行处理，每 3 个字节一组，一共是 3x8=24bit，划为 4 组，每组正好 6 个 bit：
所以，Base64 编码会把 3 字节的二进制数据编码为 4 字节的文本数据，
    长度增加 33%，好处是编码后的文本数据可以在邮件正文、网页等直接显示。
    
如果要编码的二进制数据不是 3 的倍数，最后会剩下 1 个或 2 个字节怎么办？
    Base64 用\x00 字节在末尾补足后，再在编码的末尾加上 1 个或 2个=号，表示补了多少字节，解码的时候，会自动去掉
    
Base64 是一种通过查表的编码方法，不能用于加密，
Base64 适用于小段内容的编码，比如数字证书签名、Cookie 的内容等。

由于=字符也可能出现在 Base64 编码中，但=用在 URL、Cookie 里面会造成歧义，所以，很多 Base64 编码后会把=去掉：
"""

bs64code = base64.b64encode(b'binary\x00string')
print(bs64code)
# "url safe"的 base64 编码，其实就是把字符+和/分别变成-和_
bc2 = base64.urlsafe_b64encode(b'i\xb7\x1d\xfb\xef\xff')
print(bc2)

# def pic2py(pic_path, save_path):
#     with open(pic_path, 'rb') as f:
#         print(f.read())
#         f.seek(0)
#         b64str = base64.b64encode(f.read())
#         print(b64str)
    # with open(save_path, 'wb') as f:
    #     f.write(b64str)
# pic2py(r'E:\图片\小图\c.jpg', '')