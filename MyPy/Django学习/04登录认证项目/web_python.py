from urllib.parse import parse_qs
from wsgiref.simple_server import make_server

import webauth


def application(environ, start_response):
    start_response('200 OK', [('Content-Type', 'text/html')])
    print(environ)
    path = environ['PATH_INFO']
    print(path)
    if path == '/login':
        with open('web.html', 'rb') as f:
            data = f.read()
    elif path == '/auth':
        if environ.get('REQUEST_METHOD') == 'POST':
            try:
                request_body_size = int(environ.get('CONTENT_LENGTH', 0))  # 获取请求体数据的长度,因为提交过来的数据需要用它来提取
            except ValueError:
                request_body_size = 0
            request_data = environ['wsgi.input'].read(request_body_size)
            print('>>>', request_data)
            print(environ['QUERY_STRING'])
            re_data = parse_qs(request_data)  # parse_qs可以帮我们解析数据
            print('拆解后的数据：', re_data)
        if environ.get('REQUEST_METHOD') == 'GET':
            request_data = environ['QUERY_STRING']
            print(request_data)

            re_data = parse_qs(request_data)
            print('拆解后的数据：', request_data)
            username = re_data['username']
            password = re_data['password']
            status = webauth.auth(username, password)
            if status:
                with open(r'websuccess.html', 'rb') as f:
                    data = f.read()
            else:
                re_data = b'auth error!'
    # 不管是post还是get请求都不能直接拿到数据，拿到的数据还需要我们来进行分解提取，所以我们引入urllib模块来帮我们分解
    # 我们如果直接返回中文，没有给浏览器指定编码格式，默认是gbk，所以我们需要gbk来编码一下，浏览器才能识别 data='登陆成功！'.encode('gbk')
    else:
        data = b'sorry 404,not found the page!'
    return [data]


httpd = make_server('127.0.0.1', 8080, application)
print('Serving HTTP on port 8080...')
httpd.serve_forever()
