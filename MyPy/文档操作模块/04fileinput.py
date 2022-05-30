import fileinput

f = fileinput.input(files=('a.txt', 'a_copy.txt'))  # input()--从控制台读取文件 FileInput()是一个实现类，方法同上
print(f.filename())
print(f.fileno())  # 文件描述符，未打开？-1
print(f.lineno())  # 读取的行号，未读取？0
print(f.filelineno())  # 文件行号，未读取？0
print(f.isfirstline())  # 是否第一行
print(f.isstdin())  # 是否来自控制台文件
print(f.nextfile())  # 关闭当前文件，去下一文件
f.close()