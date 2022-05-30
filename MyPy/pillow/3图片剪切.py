from PIL import Image, ImageGrab


# -----------图片截图---------
im = ImageGrab.grab((0, 0, 800, 200))   # 截取屏幕指定区域的图像
# im = ImageGrab.grab()   # 不带参数表示全屏幕截图
im.show()

# -----------图片裁剪与粘贴---------
box = (0,0,200,200)      # 定义裁剪区域
region = im.crop(box).transpose(Image.ROTATE_180)
im.paste(region, box)
im.show()