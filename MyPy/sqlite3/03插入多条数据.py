import sqlite3

con = sqlite3.connect('test.db')
cur = con.cursor()
sql = 'insert into COMPANY(ID,NAME,AGE,ADDRESS,SALARY) values(?, ?, ?, ?, ?)'
try:
    cur.executemany(sql, ((2, 'Allen', 25, 'Texas', 15000.00), (3, 'Teddy', 23, 'Norway', 20000.00), (4, 'Mark', 25, 'Rich-Mond ', 65000.00)))
    print("插入成功！")
except Exception as e:
    print("出现错误：", e)
finally:
    cur.close()
    con.commit()
    con.close()