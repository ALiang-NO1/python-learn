import tempfile
# TemporaryFile、NamedTemporaryFile、TemporaryDirectory 和SpooledTemporaryFile 是带有自动清理功能的高级接口，可用作上下文理器。
# mkstemp() 和mkdtemp() 是低级函数，使用完毕需手动清理

"""tempfile.TemporaryFile(mode='w+b', buffering=None, encoding=None, newline=None, 
    suffix=None,prefix=None, dir=None, *, errors=None)
    
tempfile.NamedTemporaryFile(mode=’w+b’, buffering=None, encoding=None, newline=None,
    suffix=None, prefix=None, dir=None, delete=True, *, errors=None)
    
tempfile.SpooledTemporaryFile(max_size=0, mode=’w+b’, buffering=None, encoding=None, 
    newline=None, suffix=None, prefix=None, dir=None, *, errors=None)
    
tempfile.TemporaryDirectory(suffix=None, prefix=None, dir=None)
tempfile.mkstemp(suffix=None, prefix=None, dir=None, text=False)
tempfile.gettempdir()   返回放置临时文件的目录的名称
tempfile.gettempdirb()  与gettempdir() 相同，但返回值为字节类型。
tempfile.gettempprefix()    返回用于创建临时文件的文件名前缀
tempfile.gettempprefixb()
"""
fp = tempfile.TemporaryFile()
fp.write(b'hello world')
fp.seek(0)
print(fp.read())
print(fp.name)
fp.close()
