import sqlite3

con = sqlite3.connect('test.db')
cur = con.cursor()
sql = 'drop user'
try:
    cur.execute(sql)
except Exception as e:
    print(e)
finally:
    cur.close()
    con.close()