import os
import shutil

def rename():   # 文件重命名
    dir = r'E:\网页\Python人工智能编程'
    for f in os.listdir(dir):
        if '[' in f:
            os.renames(os.path.join(dir, f), os.path.join(dir, f[28:]))
rename()
def move():
    dir = 'E:\win10\Pictures\电脑图片\彼岸桌面'
    os.chdir(dir)
    dirs = os.listdir(dir)
    num = len(dirs)
    step = num // 10 + 1
    li = []
    for i in range(step, num+step, step):
        li.append(i)
    print(li)
    print('■'*10, '|', num)
    count = 0
    for d in dirs:
        for f in os.listdir(d):
            shutil.move(d+'\\'+f, dir)
            os.renames(f, f.split(' 更')[0]+'.jpg')
            os.remove(d)
            count += 1
            if count in li:
                print('■', end='')
