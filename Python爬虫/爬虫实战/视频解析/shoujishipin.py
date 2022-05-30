import json, os
import requests

# 只拦截并处理返回请求
def response(flow):
    # 请求的 url
    url = 'https://api.amemv.com/aweme/v1/aweme/post/'
    # 筛选出以上面url为开头的url
    if flow.request.url.startswith(url):
        text = flow.response.text
        # 将已编码的json字符串解码为python对象
        data = json.loads(text)
        # 刚分析看到每一个视频的所有信息，都在 aweme_list 中
        video_url = data['aweme_list']
        # 设置下载路径
        path = '/Users/xx/shipin'
        # 如果文件夹不存在，则新建
        if not os.path.exists(path):
            os.mkdir(path)

        # 循环所有视频 url
        for each in video_url:
            # 视频描述
            desc = each['desc']
            url = each['video']['play_addr']['url_list'][0]
            #  设置视频名称
            filename = path+'/'+desc+'.mp4'
            # 用 request 请求视频流
            req = requests.get(url=url, verify=False)
            # 保存视频文件
            with open(filename, 'ab') as f:
                f.write(req.content)
                f.flush()
                print(filename, '下载完毕')