# 使用嵌套代码避免重复使用代码

def print_name(isChinese, name, familyname):
    def innerprint(a, b):
        print('{0} {1}'.format(a, b))

    if isChinese:
        innerprint(familyname, name)
    else:
        innerprint(name, familyname)


print_name(True, 'ruiliang', 'Jin')
