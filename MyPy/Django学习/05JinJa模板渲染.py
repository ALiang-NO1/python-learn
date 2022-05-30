from wsgiref.simple_server import make_server

from jinja2 import Template


def index():
    with open('index2.html', 'r', encoding='utf8') as f:
        data = f.read()
    template = Template(data)
    ret = template.render({'name': 'Joey', 'hobby_list': ['game', 'rock']})
    return [bytes(ret, encoding='utf8')]


URL_LIST = [('/index/', index), ]
# import pymysql
# conn = pymysql.connect(host="127.0.0.1", port=3306, user="root", passwd="xxx", db="xxx", charset="utf8")
# cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
# cursor.execute("select name, age, department_id from userinfo")
# user_list = cursor.fetchall()
# cursor.close()
# conn.close()

def run_server(environ, start_response):
    start_response('200 OK', [('Content-Type', 'text/html;charset=utf8'), ])
    url = environ['PATH_INFO']
    for i in URL_LIST:
        if i[0] == url:
            func = i[1]
            break
    if func:
        return func()
    else:
        return [bytes('404没有该页面', encoding='utf8')]


if __name__ == '__main__':
    httpd = make_server('', 8000, run_server)
    print("Serving HTTP on port 8000...")
    httpd.serve_forever()
