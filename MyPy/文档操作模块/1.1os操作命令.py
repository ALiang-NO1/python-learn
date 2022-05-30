import os

# print("系统名称：", os.name)
# print("系统路径分隔符：", os.sep)
# print("空格符：", repr(os.linesep))    # 平台使用的终止符

# ---------------文件操作---------------
# os.remove('a.txt')  # 移除单个文件

# s = os.stat('a.txt')
# print("文件大小（byte):", s.st_size)
# print("最近访问时间:", s.st_atime)
# print("最近修改时间:", s.st_mtime)
# print("创建时间:", s.st_ctime)
# for i in s:
#     print(i)

# ---------------目录操作---------------
# print(os.getcwd())  # 打印出当前工作目录
# os.chdir()    # 改变当前工作目录
# os.mkdir('os创建目录')   # 创建目录
# os.makedirs('多目录1/多目录2/多目录3')   # 创建目录树
# os.rmdir('多目录3')    # 删除空白目录
# os.removedirs('多目录1')

# ---------------os.path操作---------------
import os.path as pt

# print(pt.isabs('E:\python文档\my_py'))    # 是否为绝对目录
# print(pt.isdir('my_py'))    # 是否为目录
# print(pt.isfile('a.txt'))    # 是否是文件
# print(pt.exists('a.txt'))    # 是否存在
# print(pt.getsize('a.txt'))     # *文件字符串数量
# print(pt.abspath('a.txt'))    # 返回目录绝对路径
# print(pt.dirname('多目录1'))    # 返回目录的路径
# print(pt.getatime('a.txt'))   # 返回最后一次修改时间
# print(pt.getmtime('a.txt'))    # 返回第一次修改时间
# print(pt.join('d','my_py','test'))    # 链接路径
# print(pt.split('E:\python文档\my_py'))    # 分割出路径与文档名
# print(pt.splitext('a.txt'))    # 分割文件名
# print(os.walk('my_py'))  # walk()?

# -----遍历工作目录中的文件------

# file_list = [filename for filename in os.listdir('E:/python文档/my_py/ostest') if filename.endswith('.py')]
# for f in file_list:
#     print(f)

# ---------------压缩包zip操作---------------
# import zipfile
# z1 = zipfile.ZipFile(r'e:test.zip','w')
# z1.write('a.txt')
#
# f = zipfile.ZipFile(r'e:test.zip','r')
# for f_name in f.namelist():  # z.namelist() 会返回压缩包内所有文件名的列表。
#     print(f_name)
# z1.close()

# with zipfile.ZipFile('tt.zip', "w") as myzip:   # 压缩eggs和milk两个文件到tt.zip
#     myzip.write('eggs.txt')
# ---------------递归打印所有文件---------------
# all_file = []
# def getAllFile(path, level):
#     childFiles = os.listdir(path)
#     for file in childFiles:
#         filepath = os.path.join(path, file)
#         if os.path.isdir(filepath):
#             getAllFile(filepath, level+1)
#         all_file.append('\t'*level + filepath)
# getAllFile('E:\python文档\my_py\ostest', 0)
# for f in reversed(all_file):
#     print(f)

# ---------------shutil---------------
import shutil
# shutil.copyfile()
# shutil.copytree("多目录1", "多目录1拷贝")
# shutil.rmtree("多目录1")
# shutil.move()

# i = 2
# for n in range(4):
#     shutil.copyfile('demo1.py', 'demo'+str(i)+'.py')
#     i += 1
#     print(str(i)+'.py'+"；创建成功！")

# os.walk()
"""
os.walk(top[, topdown=True[, onerror=None[, followlinks=False]]])
参数
top -- 是你所要遍历的目录的地址, 返回的是一个三元组(root,dirs,files)。
topdown --可选，为 True，则优先遍历 top 目录，否则优先遍历 top 的子目录(默认为开启)。如果 topdown 参数为 True，walk 会遍历top文件夹，与 top 文件夹中每一个子目录。
onerror -- 可选，需要一个 callable 对象，当 walk 需要异常时，会调用。
followlinks -- 可选，如果为 True，则会遍历目录下的快捷方式(linux 下是软连接 symbolic link )实际所指的目录(默认关闭)，如果为 False，则优先遍历 top 的子目录。

root 所指的是当前正在遍历的这个文件夹的本身的地址
dirs 是一个 list ，内容是该文件夹中所有的目录的名字(不包括子目录)
files 同样是 list , 内容是该文件夹中所有的文件(不包括子目录)
"""
for root, dirs, files in os.walk(".", topdown=False):
    for name in files:
        print(os.path.join(root, name))
    for name in dirs:
        print(os.path.join(root, name))


# -----------os模块-------------
# 改名：replace() 删除：unlink() 是否有：islink() stat() path.expanduser() path.basename() path.samefile()
# os.path.splitdrive('aa:/a/b//c/d.py') os.path.realpath('多目录01') os.path.normcase('C:/user/Win10/hello//java/./b')

# -----------glob模块-----------
# import glob as g
#
# print(g.glob('*.txt'))
# print(g.glob('.a*'))
# print(g.glob('.a'))