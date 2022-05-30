from re import search, I
import csv, os

# save_file = open('ps素材盘址.csv', 'w')
# writer = csv.writer(save_file, delimiter='●')
#
# os.chdir(r'E:\PS素材\PS设计教程素材\文本文件')
# for f in os.listdir(r'E:\PS素材\PS设计教程素材\文本文件'):
#     try:
#         l = []
#         name = f.split('丨')[-1].strip(' ').strip('.txt')
#         l.append(name)
#         with open(f, 'r') as file:
#             text = file.read()
#             url = search(r'链接[：:] ?(https://pan.baidu.com/.+)', text, I).groups()[0]
#             l.append(url.rstrip(' '))
#
#             pwd = search(r'提取码[：:] ?([a-zA-Z1-9]+)', text).groups()[0]
#             l.append(pwd)
#
#             writer.writerow(l)
#     except Exception as e:
#         print('wrong:', e)
#         continue
#
# save_file.close()

with open('ps素材盘址.csv', 'r') as f:
    reader = csv.reader(f, delimiter='●')
    for line in reader:
        print(line)
