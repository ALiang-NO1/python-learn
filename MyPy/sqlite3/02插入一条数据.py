import sqlite3

con = sqlite3.connect('test.db')
cur = con.cursor()
cur.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) VALUES (1, 'Paul', 32, 'California', 20000.00 )")
print(cur.fetchall())
cur.close()
con.commit()
con.close()