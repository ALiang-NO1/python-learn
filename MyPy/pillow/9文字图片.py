from PIL import Image, ImageDraw, ImageFont

W = H = 16
text = '我的心使冰冰的'
font = ImageFont.truetype(r"C:\Windows\Fonts\SitkaI.ttc", W)  # 粗体字更好

if __name__ == '__main__':
    imgScr = Image.open('bt1.jpg')
    w, h = imgScr.size
    img_child = Image.new('RGB', (W, H))  # 子图
    img = Image.new('RGB', (W * w, H * h))  # 待填充的空图

    text_w, text_h = font.getsize('迷')
    offset_x = (W - text_w) >> 1  # 文字水平居中
    offset_y = (H - text_h) >> 1  # 文字垂直居中

    charIndex = 0
    draw = ImageDraw.Draw(img_child)  # 小图的绘制对象，用于绘制文字
    for y in range(h):
        for x in range(w):
            draw.rectangle(0, 0, W, H, fill='lightgray')  # 灰色背景
            draw.text((offset_x, offset_y), text[charIndex], font=font, fill=imgScr.getpixel((x, y)))
            img.paste(img_child, (x * W, y * H))  # 将子图填到空图

            charIndex += 1
            if charIndex == len(text):
                charIndex = 0

    img.save('E:\\')
