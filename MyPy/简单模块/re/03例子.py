import re

s = 'first 1 second 2 third 3'
result_a = re.findall('\w+', s)
result_b = re.finditer('\w+', s)
print("-------find���н����")
print(result_a)
print("-------finditer���н����")
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
print("�����ַ���: ", a)
print("���ַ����룺", b)

s = '2004-959-500  # ����һ������ĵ绰����'
# a0 = re.sub(r'#.*$', '', s)
# print(a0)

a = re.subn(r'#.*$', '', s)
print('subn()->', a)
print("�滻�Ľ����", a[0])
print("�滻�Ĵ�����", a[1])

dirm = re.match(r'^(\d{3})-(\d{3,8})$', '010-12345')
print(dirm)
print(dirm.group(0))
print(dirm.group(1))
print(dirm.group(2))

file_content = "<body><h1>hahahaha</h1></body>"
judge_rule = r"^<(?P<p1>\w*)><(?P<p2>\w*)>\w*</(?P=p2)></(?P=p1)>$"  # �ر�ע����һ��������ʽ
try:
    temp = re.match(judge_rule, file_content)
    if temp is None:  # ��һ��ȷ����������
        print("match()�ķ���ֵΪ��")
    print(temp.group())
    print(temp.group(1))
    print(temp.group(2))
except AttributeError:
    print("����������ʽ��ǩ�Ƿ��Ӧ")
except Exception as result:
    print("����ԭ��", result)
s = '2335532@qq.com'
a = re.search(p, s)
print(a)