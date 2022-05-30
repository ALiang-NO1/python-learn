from collections import deque, namedtuple, defaultdict, OrderedDict, Counter

point = namedtuple('point', ['x', 'y'])
p = point(1, 2)
print('x坐标：', p.x)
print('y坐标：', p.y)
print(isinstance(p.x, point))
print(isinstance(p.x, tuple))
circle = namedtuple('circle', ['x', 'y', 'r'])
c = circle(3, 5, 2)
print('圆半径', c.r)

print()
print('----------dequee--------------')
q = deque(['a', 'b', 'c'])  # 类似列表
q.append('d')
q.appendleft('e')
print(q)
print(q[0])
print(q.pop())

print()
print('-------defaultdict--------')
dd = defaultdict(lambda: 'N/A')
dd['key1'] = 'haha'
print(dd['key1'])
print(dd['key2'])

print()
print('--------OrderdDict-------')
od = OrderedDict()  # 先进先出（FIFO）
od['z'] = 1
od['y'] = 2
od['x'] = 3
print(list(od.keys()))

# class LastUpdatedOrderedDict(OrderedDict):
#  def __init__(self, capacity):
#      super(LastUpdatedOrderedDict, self).__init__()
#      self._capacity = capacity
#  def __setitem__(self, key, value):
#      containsKey = 1 if key in self else 0
#      if len(self) - containsKey >= self._capacity:
#          last = self.popitem(last=False)
#          print('remove:', last)
#      if containsKey:
#          del self[key]
#          print('set:', (key, value))
#      else:
#          print('add:', (key, value))
#          OrderedDict.__setitem__(self, key, value)

print()
print('-------------Counter计数器-----------')
c = Counter()
for chr in 'programming':
    c[chr] = c[chr] + 1
print(c)