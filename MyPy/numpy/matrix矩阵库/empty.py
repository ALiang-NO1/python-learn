from numpy import matlib as mt

print("返回矩阵，填充随机数")
print("empty")
print(mt.empty((3, 4), dtype=int, order='C'))
print("zeros")
print(mt.zeros((3, 5)))
print("ones")
print(mt.ones(9))