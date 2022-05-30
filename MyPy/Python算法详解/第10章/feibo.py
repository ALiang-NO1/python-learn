#coding=utf-8
def fib_list(n) :
  if n == 1 or n == 2 :
    return 1
  else :
    m = fib_list(n - 1) + fib_list(n - 2)
    return m
print("**********请输入要打印的斐波拉契数列项数n的值***********")
try :
  n = int(input("enter:"))
except ValueError :
  print("请输入一个整数！")
  exit()
list2 = [0]
tmp = 1
while(tmp <= n):
  list2.append(fib_list(tmp))
  tmp += 1
print(list2)