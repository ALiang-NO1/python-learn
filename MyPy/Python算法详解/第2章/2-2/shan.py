#定义元组“tup”
tup = ('Google', 'Toppr', 1997, 2000)
print (tup)        	#输出元组“tup”中的元素
del tup;           	#删除元组“tup”
#因为元组“tup”已经被删除，所以不能显示里面的元素
print ("元组tup被删除后，系统会出错！")
print (tup)        	#这行代码会出错
