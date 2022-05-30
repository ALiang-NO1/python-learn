import numpy as np

x = np.array([[1], [2], [3]])
y = np.array([4, 5, 6])

print('对 y 广播 x：')
b = np.broadcast(x, y)
print(b)
r, c = b.iters  # 它拥有 iterator 属性，基于自身组件的迭代器元组

# Python3.x 为 next(context) ，Python2.x 为 context.next()
print(next(r), next(c))
print(next(r), next(c))

print('广播对象的形状：')
print(b.shape)

c = np.empty(b.shape)
print('手动使用 broadcast 将 x 与 y 相加：')
print(c.shape)

c.flat = [u + v for (u, v) in b]
print('调用 flat 函数：')
print(c)

# 获得了和 NumPy 内建的广播支持相同的结果
print('x 与 y 的和：')
print(x + y)