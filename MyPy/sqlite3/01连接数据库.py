import sqlite3

con = sqlite3.connect('test.db')    # 创建连接
cur = con.cursor()   # 创建游标
sql = '''CREATE TABLE COMPANY(
    ID INT PRIMARY KEY NOT NULL,
    NAME TEXT NOT NULL,
    AGE INT NOT NULL,
    ADDRESS CHAR(50),
    SALARY REAL);'''

# sql = 'create table users(num integer primary key auto_increment, name varchar not null, age integer)'
try:
    cur.execute(sql)
    print("创建成功！")
except Exception as e:
    print("出现错误：", e)
finally:
    cur.close()
    con.close()