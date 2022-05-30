from PIL import Image

img = Image.open('bt1.jpg')
img.show()
# img.save("E:\\")
print("图像属性:", img.format, "宽高:", img.size, "模式:", img.mode)
img = img.resize((100, 100))    # 设置图片宽、高
print(img.size)

# h = img.histogram()
# print("图片直方图：", h)

def test_gif():
    img = Image.open('CSDN.gif')
    print('gif图测试，帧数：', img.tell())
    img.seek(1)  # skip to the second frame
    try:
        while 1:
            img.seek(img.tell()+1)
            print(img.tell()+1)
            # do something to img
    except EOFError:
        pass
test_gif()