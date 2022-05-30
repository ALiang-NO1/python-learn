from tempfile import TemporaryDirectory
from tempfile import TemporaryFile

# with TemporaryDirectory('temp') as temp_dir:
#     print(temp_dir)     # 程序终止文件删除
#     input("输入中......等待删除。按下任意键删除文档")

with TemporaryFile('w+') as file:
    file.write("这是一个临时文档")
    file.seek(8)
    print(file.readline())