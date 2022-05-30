def createtable():
    import pymysql
    conn = pymysql.connect(
        '127.0.0.1',
        prot=3306,
        user='root',
        password='666',
        database='db1',
        charset='utf8'
    )
    cursor = conn.connect(pymysql.cursors.DictCursor)
    sql = """
        -- 创建表
        create table userinfo(id int primary key auto_increment,username char(20) not null unique,password char(20) not null);
        -- 插入数据
        insert into userinfo(username,password) values('chao','666'),('sb1','222');
        """
    cursor.execute(sql)
    conn.commit()
    cursor.close()
    conn.close()
