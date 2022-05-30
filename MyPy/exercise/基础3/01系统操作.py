# import sys
# print(sys.argv)
# sys.stderr.write('Warning, log file not found starting a new one\n')

# import zlib  # 数据压缩模块，还有：gzip, bz2, lzma, zipfile, tarfile
# s = b'witch which has which witches wrist watch'
# t = zlib.compress(s)
# print('len(s):', len(s), ' len(t):', len(t), ' t:', t)
# print('decompressed t:', zlib.decompress(t))
# print(zlib.crc32(s))

# from timeit import Timer  # 精确计时模块，低精度：profile, pstats
# print(Timer('t=a; a=b; b=t', 'a=1; b=2').timeit())
# print(Timer('a,b = b,a', 'a=1; b=2').timeit())

# def average(values):
#     """Computes the arithmetic mean of a list of numbers.
#     >>> print(average([20, 30, 70]))
#     40.0
#     """
#     return sum(values) / len(values)
# import doctest  # 质量控制，测试函数
# doctest.testmod()

# import reprlib  # 格式化输出，缩略显示
# rp = reprlib.repr(set('supercalifragilisticexpialidocious'))
# print(rp)
#
# import pprint  # 格式化输出，美化输出
# t = [[[['black', 'cyan'], 'white', ['green', 'red']], [['magenta', 'yellow'], 'blue']]]
# pprint.pprint(t, width=30)

# import textwrap  # 格式化输出，
# doc = """这是一段文本：The wrap() method is just like fill() except that it returns
# a list of strings instead of one big string with newlines to separate the wrapped lines."""
# print(textwrap.fill(doc, width=40))

# import locale  # 格式化输出，地域文化数据
# lc = locale.setlocale(locale.LC_ALL, 'English_United States.1252')
# print(lc)
# conv = locale.localeconv()
# x = locale.format('%d', 123456.78, grouping=True)
# print(x)
# fstr = locale.format_string('%s%.*f', (conv['currency_symbol'], conv['frac_digits'], 123456.78), grouping=True)
# print(fstr)

# from string import Template  # 模板，格式化占位符
# t = Template('${village}folk send $$10 to $cause.')
# sub = t.substitute(village='Nottingham', cause='the ditch fund')
# print(sub)
# safe_sub = t.safe_substitute(village='Manhatton')
# print(safe_sub)

# import time, os.path  # 格式化输出，修改图片名
# from string import Template
# photofiles = ['img_1074.jpg', 'img_1076.jpg', 'img_1077.jpg']
# class BatchRename(Template):
#     delimiter = '%'
# fmt = input('Enter rename style (%d-date %n-seqnum %f-format): ')  # ALiang_%n%f
# t = BatchRename(fmt)
# data = time.strftime('%d%b%y')
# for i, filename in enumerate(photofiles):
#     base, ext = os.path.splitext(filename)
#     newname = t.substitute(d=data, n=i, f=ext)
#     print(f'{filename} --> {newname}')

# import zipfile
# with open('aa.txt', 'w') as f:
#     f.write('abcde'*10)
# f = zipfile.ZipFile('test.zip', 'w')
# f.write('aa.txt')
# f.close()
# import struct  # 于处理不定长度的二进制记录格式
# with open('test.zip', 'rb') as f:
#     data = f.read()
# start = 0
# for i in range(3):
#     start += 14
#     fields = struct.unpack('<IIIHH', data[start: start+16])
#     crc32, comp_size, uncomp_size, filenamesize, extra_size = fields
#     start += 16
#     filename = data[start: start+filenamesize]
#     start += filenamesize
#     extra = data[start: start+extra_size]
#     print(filename, hex(crc32), comp_size, uncomp_size)

# import bisect  # 操作排序列表
# scores = [(100, 'perl'), (200, 'tcl'), (400, 'lua'), (500, 'python')]
# bisect.insort(scores, (300, 'ruby'))
# print(scores)

# from heapq import heapify, heappop, heappush  # 实现堆（用于需要重复访问最小元素而不希望运行完整列表排序）
# data = [1, 3, 5, 7, 9, 2, 4, 6, 8, 0]
# heapify(data)
# print(data)
# heappush(data, -5)
# print(data)
# print([heappop(data) for i in range(3)])

# from decimal import Decimal, getcontext  # 提供了运算所需要的足够精度
# print(round(.70*1.05, 2))
# print(round(Decimal('0.70')*Decimal('1.05'), 2))
# print(1.00%0.10)
# print(Decimal('0.1')*10)
# getcontext().prec = 36
# print(Decimal(1)/Decimal(7))