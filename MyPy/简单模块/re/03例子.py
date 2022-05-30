import re

s = 'first 1 second 2 third 3'
result_a = re.findall('\w+', s)
result_b = re.finditer('\w+', s)
print("-------find运行结果：")
print(result_a)
print("-------finditer运行结果：")
for i in result_b:
    print(i.group())

s = "a   hello123word\tmother"
print(re.findall("\w*", s, re.S))

print(re.search('\w*', 'Hello Word'))
# p = '\d*'
# s = '12345weER24_.!@'
# = r'^[1-9]\d{4,9}@qq.com$'
# a = re.search(p, s)
# print(a)
# print(a.group())
# print(a.span())
# print(a.start())

# s = 'first 11 second 22 third 33'
p = '\d+'
a = re.split(p, s)
b = re.split('', s)
print("按数字分离: ", a)
print("按字符分离：", b)

s = '2004-959-500  # 这是一个国外的电话号码'
# a0 = re.sub(r'#.*$', '', s)
# print(a0)

a = re.subn(r'#.*$', '', s)
print('subn()->', a)
print("替换的结果：", a[0])
print("替换的次数：", a[1])

dirm = re.match(r'^(\d{3})-(\d{3,8})$', '010-12345')
print(dirm)
print(dirm.group(0))
print(dirm.group(1))
print(dirm.group(2))

file_content = "<body><h1>hahahaha</h1></body>"
judge_rule = r"^<(?P<p1>\w*)><(?P<p2>\w*)>\w*</(?P=p2)></(?P=p1)>$"  # 特别注意这一条正则表达式
try:
    temp = re.match(judge_rule, file_content)
    if temp is None:  # 进一步确定错误类型
        print("match()的返回值为空")
    print(temp.group())
    print(temp.group(1))
    print(temp.group(2))
except AttributeError:
    print("请检查正则表达式标签是否对应")
except Exception as result:
    print("出错原因：", result)
s = '2335532@qq.com'
a = re.search(p, s)
print(a)