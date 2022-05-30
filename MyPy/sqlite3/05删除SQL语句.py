import sqlite3

con = sqlite3.connect('test.db')
cur = con.cursor()
sql = "DELETE from COMPANY where ID=?"
try:
    cur.execute(sql, (2,))
    print("删除成功！")
except Exception as e:
    print("出现错误：", e)
finally:
    cur.close()
    con.commit()
    con.close()