from MyQR import myqr

myqr.run(
    words='https://baidu.com',
    picture='C:\\Users\\jinyj\\Desktop\\p1.png',
    # 或picture=r'C:\Users\jinyj\Desktop\p1.png',省去双斜杠
    colorized=True,
)
myqr.run(
    words='网址链接或者字符串，不支持中文',
    # 扫描二维码后，显示的内容，或是跳转的链接
    version=5,  # 设置容错率
    level='H',  # 控制纠错水平，范围是L、M、Q、H，从左到右依次升高
    picture='7cf0bfb0bb10ea94d19455a13f62a05.png',  # 图片所在目录，可以是动图
    colorized=True,  # 黑白(False)还是彩色(True)
    contrast=1.0,  # 用以调节图片的对比度，1.0 表示原始图片。默认为1.0。
    brightness=2.0,  # 用来调节图片的亮度，用法同上。
    save_name='cxn.png',  # 控制输出文件名，格式可以是 .jpg， .png ，.bmp ，.gif
    save_dir=r'E:/',  # 图片存储位置
)