import re
import os

def list_word(file):
    with open(file, encoding='UTF-8') as f:
        text = f.read()
        return text.split()

def save2txt(path, data):
    print('正在保存信息...')
    with open(os.path.join(path, 'count.txt'), 'w', encoding='utf-8')as f:
        for i in data:
            f.write(str(i))
            f.write('\n')
        print('保存成功！')

file = 'E:\\CET6.txt'
result = list_word(file)
words = [i.lower() for i in re.findall('[a-zA-Z]+', str(result)) if len(i) > 2]
d = dict()
common_word = ['the', 'and', 'for', 'are', 'that', 'you', 'not', 'one', 'this', 'people']
for word in words:
    if (word not in common_word) & (not (word in d)):
        d[word] = words.count(word)     # if word not in common_word: d[word] = d.get(word, 0) + 1
        data = sorted(d.items(), key=lambda x: x[1], reverse=True)
path = 'E:'
save2txt(path, data)