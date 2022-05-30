from wsgiref.simple_server import make_server


def application(environ, start_response):
    """

    :param environ:是全部加工好的请求信息，加工成了一个字典
    :param start_response:帮你封装响应信息的（响应行和响应头）
    :return:
    """
    start_response('200 OK', [('k1', 'v1'), ])
    print(environ)
    print(environ['PATH_INFO'])
    return [b'<h2>Hello, Web!</h2>']


httpd = make_server('127.0.0.1', 8003, application)
print('Serving HTTP on prot 8080....')
httpd.serve_forever()
