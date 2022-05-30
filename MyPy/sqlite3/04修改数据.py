import sqlite3

con = sqlite3.connect('test.db')
cur = con.cursor()
sql = "UPDATE COMPANY set SALARY = 25000.00 where ID=1"
try:
    cur.execute(sql)
    print('suc')
except Exception as e:
    print(e)
finally:
    cur.close()
    con.close()