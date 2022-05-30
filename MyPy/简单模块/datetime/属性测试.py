import datetime, time

print("-----当前时间------")
t = datetime.datetime.now()  # 年-月-日 时-分-秒.微秒
print(t)
print(t.date())
print(t.time())
print(t.utctimetuple())  # struct_time

print("------当前时间戳today------")
print("当前时间戳对应日期：", datetime.date.today())

dt1 = datetime.datetime.fromtimestamp(10000)    # 将时间戳转为datetime对象
dt2 = datetime.datetime.fromtimestamp(time.time())      # 相当于将秒转为日期
print('time.time:', time.time())    # 它表示从 Unix 纪元（1970年1月1日0点）到执行代码那一刻所经历的时间的秒数，这个数字称为UNIX纪元时间戳
print('纪元秒（10000）对应时间:', dt1)
print('现在纪元秒转当前时间:', dt2)

print("-----------timedelte()------------")
now = datetime.datetime.now()
print('datetime.now():', now)
newdate = now + datetime.timedelta(hours=10)
print('timedelta(10):', newdate)    # 返回一个 timedelta 类型的数据，它表示一段时间而不是一个时刻

newdate = now - datetime.timedelta(days=1)
print(newdate)

print("------时间time--------")
t3 = datetime.time(19, 42, 34, 12)
print(t3)
print("易读形式：", time.ctime())
print("计算机易处理时间：", time.gmtime())
print("自定义时间：", time.strftime("%Y, %m, %d, %c"))
# print("将字符串转为变量：", time.strptime())

# print("-----程序计时---")
# start = time.perf_counter()
# end = time.perf_counter()
# time.sleep(2)
# time = end - start
# print("程序运行时间为{0}".format(time))