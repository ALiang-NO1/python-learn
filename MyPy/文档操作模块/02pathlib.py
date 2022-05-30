from pathlib import Path, PurePosixPath, PureWindowsPath

# 列出子目录
p = Path('../')
print([x for x in p.iterdir() if x.is_dir()])
# 列出上级目录树下的所有 Python 源代码文件
print(list(p.glob('**/*.py'))[0])
# 移动目录
p = Path('/etc')
q = p / 'init.d' / 'reboot'  # 斜杠 / 操作符有助于创建子路径
print(q.resolve(), q.exists())
# 读取文件
with q.open('r') as f: f.readline()

# ------------纯路径: 子类有 PurePosixPath PureWindowsPath------------
from pathlib import PurePath as pp
pp('struct.py')
pp('foo', 'a/b', 'bar')
pp('foo', 'a\b', 'bar')
pp()
pp('C:user', 'D:fun')
pp('/a', '/b', 'c')
pp('C:/Windows', 'Program Files')
pp('a//b', 'c/./d', 'e/../g')  # . / // 都会去掉，除了..

# 路径是不可变并可哈希的。相同风格的路径可以排序与比较
print(PurePosixPath('foo') == PurePosixPath('FOO'))
print(PureWindowsPath('FOO') in {PureWindowsPath('foo')})
print(PureWindowsPath('C:') < PureWindowsPath('d:'))

# 访问路径独立的部分
print(p.parts)
# 驱动目录
print(p.drive)
print(pp('d:program').drive)
print(pp('//host/share/foo.txt').drive)
print(pp('e:/win10').root)  # 根
print(pp('//host/share').anchor)  # 驱动器和根的联合
# 路径最后一个组件
print(pp('a/b/c.py').name)
# 文件后缀
print(pp('a//b/c.csv').suffix)
print(pp('a//b/c.csv.txt.gz').suffixes)
# 最后一个组件除去后缀
print(pp('a//b/c.csv.txt.gz').stem)
# 将反斜杠转斜杠
print(pp('a//b/c.csv.txt.gz').as_posix())
# 转文件路径
print(pp('a/b/c.csv.txt.gz').as_uri())
# 是否是觉得路径
print(pp('a/b/c.csv.txt.gz').is_absolute())
# 是否被Windows保留
print(pp('nul').is_reserved())
# 链接路径
print(pp('/etc').joinpath('a', 'b'))
# 匹配路径
print(pp('a/b/test.py').match('b/*.py'))
print(pp('a/b/test.py').match('/*.py'))
# 相对路径获取
print(pp('a/b/c/test.py').relative_to('a'))
# 修改文件名
print(pp('a/b/c/d.tar.gz').with_name('setup.py'))
# 修改文件后缀
print(pp('a/b/c/d.tar.gz').with_suffix('.bz2'))
# 当前目录
from pathlib import Path as pt
print(pt.cwd())
# 家目录
print(pt.home())
# 文件大小
print(pt('setup.py').stat().st_size)
# 改变文件模式
p.chmod(0)
# 完整路径，相对家目录？？
print(pt('~/ffmpeg.md').expanduser())
# glob匹配
print(sorted(pt('.').glob('*.md')))
# 是否是文档
print(pt('grab.py').is_file())
# 按字节、文本读取
print(pt('grab.py').read_bytes())
print(pt('grab.py').read_text())
# 重命名
p = pt('test.txt')
p.open('a+').write('\nnewline!')
p.rename('aa.txt')
# 绝对路径
print(p.resolve())
# 重命名文件或目录
p.replace('bb.txt')
# 按通配符匹配文件
print(sorted(pt().rglob('*.md')))
# 移除目录
pt.rmdir(pt('aa'))
p.unlink()
# 判断是否是同文档
p.samefile(q)
# 写文本或字节
p.write_text('hello')
p.write_bytes(b'a.xls')
