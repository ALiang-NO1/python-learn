import os
from PIL import Image, ImageDraw, ImageFont


def text2pic(file_dir):
    for root, dirs, files in os.walk(file_dir):  # 列出目录下所有的文件
        for file in files:
            if not file.endswith('.jpg'):
                continue
            pic_path = os.path.join(file_dir, file)
            image = Image.open(pic_path)
            # 获取图片尺寸
            width, height = image.size

            # 设置需要显示的字体，# Mac os字体路径 /System/Library/Fonts/ windows系统字体路径一般为C:\Windows\Fonts
            fontpath = r"C:\Windows\Fonts\SitkaI.ttc"
            font = ImageFont.truetype(fontpath, 20)  # 设置字体和字体大小
            draw = ImageDraw.Draw(image)
            # 添加水印
            draw.text(xy=(1/30 * width, 2/5 * height), text=u'@Python知识圈', fill=(255, 0, 0), font=font)
            image.save(os.path.join(file_dir, "watermark_%s" % file))


if __name__ == '__main__':
    file_dir = r'E:\python文档\MyPy\pillow'
    text2pic(file_dir)
