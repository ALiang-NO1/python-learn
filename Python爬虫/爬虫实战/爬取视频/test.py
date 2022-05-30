import requests
import os
import subprocess
# 视频解析：https://jx.618g.com/url=
# cmd执行合成视频：copy /b *.ts test.mp4
"""通过对第二层下载得到的m3u8文件进行分析我们可以发现这一行代码：EXT-X-KEY:METHOD=AES-128,URI="key.key"
此网站采用AES方法对所有ts文件进行了加密，其中METHOD=ASE-128 ：说明此视频采用ASE-128方式进行加密，URI=“key.key”：代表key的地址"""

for i in range(1, 2):
    url = 'https://stream.lystgf.com/tv_adult/avid5cf789a296746/240/ts/avid5cf789a296746-%s.ts' % i
    response = requests.get(url).content
    filename = '%s.ts' % i
    if not os.path.exists(filename):
        with open(filename, 'wb') as f:
            f.write(response)
            print(filename, "保存成功！")