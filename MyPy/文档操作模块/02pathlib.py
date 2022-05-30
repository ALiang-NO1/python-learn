from pathlib import Path, PurePosixPath, PureWindowsPath

# �г���Ŀ¼
p = Path('../')
print([x for x in p.iterdir() if x.is_dir()])
# �г��ϼ�Ŀ¼���µ����� Python Դ�����ļ�
print(list(p.glob('**/*.py'))[0])
# �ƶ�Ŀ¼
p = Path('/etc')
q = p / 'init.d' / 'reboot'  # б�� / �����������ڴ�����·��
print(q.resolve(), q.exists())
# ��ȡ�ļ�
with q.open('r') as f: f.readline()

# ------------��·��: ������ PurePosixPath PureWindowsPath------------
from pathlib import PurePath as pp
pp('struct.py')
pp('foo', 'a/b', 'bar')
pp('foo', 'a\b', 'bar')
pp()
pp('C:user', 'D:fun')
pp('/a', '/b', 'c')
pp('C:/Windows', 'Program Files')
pp('a//b', 'c/./d', 'e/../g')  # . / // ����ȥ��������..

# ·���ǲ��ɱ䲢�ɹ�ϣ�ġ���ͬ����·������������Ƚ�
print(PurePosixPath('foo') == PurePosixPath('FOO'))
print(PureWindowsPath('FOO') in {PureWindowsPath('foo')})
print(PureWindowsPath('C:') < PureWindowsPath('d:'))

# ����·�������Ĳ���
print(p.parts)
# ����Ŀ¼
print(p.drive)
print(pp('d:program').drive)
print(pp('//host/share/foo.txt').drive)
print(pp('e:/win10').root)  # ��
print(pp('//host/share').anchor)  # �������͸�������
# ·�����һ�����
print(pp('a/b/c.py').name)
# �ļ���׺
print(pp('a//b/c.csv').suffix)
print(pp('a//b/c.csv.txt.gz').suffixes)
# ���һ�������ȥ��׺
print(pp('a//b/c.csv.txt.gz').stem)
# ����б��תб��
print(pp('a//b/c.csv.txt.gz').as_posix())
# ת�ļ�·��
print(pp('a/b/c.csv.txt.gz').as_uri())
# �Ƿ��Ǿ���·��
print(pp('a/b/c.csv.txt.gz').is_absolute())
# �Ƿ�Windows����
print(pp('nul').is_reserved())
# ����·��
print(pp('/etc').joinpath('a', 'b'))
# ƥ��·��
print(pp('a/b/test.py').match('b/*.py'))
print(pp('a/b/test.py').match('/*.py'))
# ���·����ȡ
print(pp('a/b/c/test.py').relative_to('a'))
# �޸��ļ���
print(pp('a/b/c/d.tar.gz').with_name('setup.py'))
# �޸��ļ���׺
print(pp('a/b/c/d.tar.gz').with_suffix('.bz2'))
# ��ǰĿ¼
from pathlib import Path as pt
print(pt.cwd())
# ��Ŀ¼
print(pt.home())
# �ļ���С
print(pt('setup.py').stat().st_size)
# �ı��ļ�ģʽ
p.chmod(0)
# ����·������Լ�Ŀ¼����
print(pt('~/ffmpeg.md').expanduser())
# globƥ��
print(sorted(pt('.').glob('*.md')))
# �Ƿ����ĵ�
print(pt('grab.py').is_file())
# ���ֽڡ��ı���ȡ
print(pt('grab.py').read_bytes())
print(pt('grab.py').read_text())
# ������
p = pt('test.txt')
p.open('a+').write('\nnewline!')
p.rename('aa.txt')
# ����·��
print(p.resolve())
# �������ļ���Ŀ¼
p.replace('bb.txt')
# ��ͨ���ƥ���ļ�
print(sorted(pt().rglob('*.md')))
# �Ƴ�Ŀ¼
pt.rmdir(pt('aa'))
p.unlink()
# �ж��Ƿ���ͬ�ĵ�
p.samefile(q)
# д�ı����ֽ�
p.write_text('hello')
p.write_bytes(b'a.xls')
