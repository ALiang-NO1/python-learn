import urllib.request  # 导入模块
import urllib.parse
import json
class Trs:
    def __init__(self):
        url = "http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule"
        content = input("翻译内容：")
        data = {}
        data['i'] = content
        data['from'] = 'AUTO'
        data['to'] = 'AUTO'
        data['smartresult'] = 'dict'
        data['client'] = 'fanyideskweb'
        data['salt'] = '15823411455528'
        data['sign'] = 'd03024a90896a5eb31a74a9344657b0e'
        data['doctype'] = 'json'
        data['version'] = '2.1'
        data['keyfrom'] = 'fanyi.web'
        data['action'] = 'FY_BY_REALTlME'
        data = urllib.parse.urlencode(data).encode('utf-8')
        r = urllib.request.Request(url, data)
        r.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                                   'Chrome/79.0.3945.130 Safari/537.36')
        response = urllib.request.urlopen(r)
        html = response.read().decode('utf-8')
        trs = json.loads(html)
        result = trs['translateResult'][0][0]['tgt']
        print("翻译结果：", result)
if __name__ == "__main__":
    a = Trs()