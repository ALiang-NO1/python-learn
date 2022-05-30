"""在8*8的国际象棋上，摆放八个皇后，使其不能相互攻击，即任意两个皇后不能在同一行，同一列，同意斜线上，问有多少种摆法？"""
n = int(input())
x = []  # 一个解
X = []  # 一组解
# 检测冲突：判断x[k]是否与之前的x[0]~x[k-1]冲突
def conflict(k):
    global x
    for i in range(k):  # 遍历前面的x[0]~x[k-1]
        if x[i] == x[k] or abs(x[i]-x[k]) == abs(i-k):
            return True
    return False
# 用子集树模板
def queens(k):
    global n
    global X,x
    if k >= n:
        X.append(x[:])  # 超出最低行时保存一个解
    else:
        for i in range(n):  # 遍历n~n-1列
            x.append(i)     # 皇后置于第i列,入栈
            if not conflict(k):   # 剪枝
                queens(k+1)
            x.pop() # 出栈
# 可视化解(X代表皇后)
def show(x):
    global n
    for i in range(n):
        print('. '*(x[i])+'Q '+'. '*(n-x[i]-1))
# 测试
queens(0)
print(X[-1], '\n')
print(len(X))   # 解的个数
show(X[-1])