def auth(username, password):
    import pymysql
    conn = pymysql.connect(
        '127.0.0.1',
        prot=3306,
        user='root',
        password='666',
        database='db1',
        charset='utf8'
    )
    print('UserInfo:', username, password)
    cursor = conn.connect(pymysql.cursors.DictCursor)
    sql = 'select * from userinfo where username=%s and password=%s'
    res = cursor.execute(sql, [username, password])
    if res:
        return True
    else:
        return False
