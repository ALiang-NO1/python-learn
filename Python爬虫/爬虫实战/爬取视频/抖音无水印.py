import re
from all import *

share_url = "https://v.douyin.com/JePfx5f/"
# 获取 itemId、dytk
content = rq(share_url).content
itemId = re.findall(r"(?<=itemId:\s\")\d + ", str(content))
dytk = re.findall(r"(?<=dytk:\s\")(.*?)(?=\")", str(content))
# 组装视频长链接
long_url = "https://www.iesdouyin.com/web/api/v2/aweme/iteminfo/?item_ids=" + itemId[0] + "&dytk=" + dytk[0]
# 请求长链接，获取 play_addr
video_open_html = rq(long_url).text
uri = re.findall(r'(?<=\"uri\":\")\w{32}(?=\")', str(video_open_html))
# video_id 是长链接唯一变动的，提取出 uri 进行组装得到最终链接
play_addr = "https://aweme.snssdk.com/aweme/v1/play/?video_id=" + uri[0] + \
    "&line=0&ratio=540p&media_type=4&vr_type=0&improve_bitrate=0&is_play_url=1&is_support_h265=0&source=PackSourceEnum_PUBLISH"
# 保存短视频
with open("douyin.mp4", "wb") as file:
    file.write(rq(play_addr).content)
    file.close()
    print("抖音无水印视频下载完成！")