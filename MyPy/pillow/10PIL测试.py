import numpy as np
from PIL import Image,ImageFont,ImageDraw

# im=Image.new('RGB',(16,16))
draw=ImageDraw.Draw()
font=ImageFont.truetype(r"C:\Windows\Fonts\FZSTK.TTF")
print(font.getsize('我'))
print(font.getsize('个迷糊'))

