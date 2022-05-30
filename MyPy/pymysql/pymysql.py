import pymysql

# 创建链接
conn = pymysql.connect(host='197.0.0.1', port=3306, database='test', user='root', password='root')
# 创建索引
cursor = conn.cursor()
# 查找
sql = "select * from userinfo"
cursor.execute(sql)
r = cursor.fetchone()
# 获取所有
# r = cursor.fetchall()
print(r)

# 增加
sql = "insert into userinfo(username,password) values(%s,%s)"
# 返回受影响的行数
r = cursor.execute(sql,['root','123456'])
print(r)
conn.commit()
cursor.close()
conn.close()

# 批量增加  executemany
sql = "insert into userinfo(username,password) values(%s,%s)"
# laoer  laoer_pass
# laosan laosan_pass
r = cursor.executemany(sql,[('laoer','laosan'),('laoer_pass','laosan_pass')])
print(r)
conn.commit()
cursor.close()
conn.close()

# 修改
sql = "update userinfo set password=%s where username ='tang'"
r = cursor.executemany(sql,('456789',))
conn.commit()
cursor.close()
conn.close()

# 删除
sql = "delete from userinfo WHERE username=%s"
r = cursor.executemany(sql,('root',))
conn.commit()
cursor.close()
conn.close()
