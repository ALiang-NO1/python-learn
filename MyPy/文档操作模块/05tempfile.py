import tempfile
# TemporaryFile��NamedTemporaryFile��TemporaryDirectory ��SpooledTemporaryFile �Ǵ����Զ������ܵĸ߼��ӿڣ�������������������
# mkstemp() ��mkdtemp() �ǵͼ�������ʹ��������ֶ�����

"""tempfile.TemporaryFile(mode='w+b', buffering=None, encoding=None, newline=None, 
    suffix=None,prefix=None, dir=None, *, errors=None)
    
tempfile.NamedTemporaryFile(mode=��w+b��, buffering=None, encoding=None, newline=None,
    suffix=None, prefix=None, dir=None, delete=True, *, errors=None)
    
tempfile.SpooledTemporaryFile(max_size=0, mode=��w+b��, buffering=None, encoding=None, 
    newline=None, suffix=None, prefix=None, dir=None, *, errors=None)
    
tempfile.TemporaryDirectory(suffix=None, prefix=None, dir=None)
tempfile.mkstemp(suffix=None, prefix=None, dir=None, text=False)
tempfile.gettempdir()   ���ط�����ʱ�ļ���Ŀ¼������
tempfile.gettempdirb()  ��gettempdir() ��ͬ��������ֵΪ�ֽ����͡�
tempfile.gettempprefix()    �������ڴ�����ʱ�ļ����ļ���ǰ׺
tempfile.gettempprefixb()
"""
fp = tempfile.TemporaryFile()
fp.write(b'hello world')
fp.seek(0)
print(fp.read())
print(fp.name)
fp.close()
