import requests

url = ''
headers = {
    # 这里填resquest headers 内容
}
session = requests.Session()
source = requests.get(url, headers=headers, verify=False).content.decode()