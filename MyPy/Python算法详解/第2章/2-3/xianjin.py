import collections

dic = collections.OrderedDict()
dic['k1'] = 'v1'
dic['k2'] = 'v2'
dic['k3'] = 'v3'
print(dic.popitem(),dic)
print(dic.popitem(),dic)

# 输出：('k3', 'v3') OrderedDict([('k1', 'v1'), ('k2', 'v2')])
#      ('k2', 'v2') OrderedDict([('k1', 'v1')])