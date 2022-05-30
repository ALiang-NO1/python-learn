import sqlite3

con = sqlite3.connect('test.db')
cur = con.cursor()
sql = "SELECT id, name, address, salary from COMPANY"
try:
    data = cur.execute(sql)
    # for row in data:
    #     print("ID = ", row[0])
    #     print("NAME = ", row[1])
    #     print("ADDRESS = ", row[2])
    #     print("SALARY = ", row[3], "\n")
    # print("------第一种-----")
    print(cur.fetchall())
    # print("------第二种-----")
    # print(cur.fetchone())
    # print("------第三种-----")
    # print(cur.fetchmany(3))
except Exception as e:
    print("出现错误：", e)
finally:
    cur.close()
    con.close()