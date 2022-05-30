n = 5  # 8太慢了，改为5
p = [(-2, 1), (-1, 2), (1, 2), (2, 1), (2, -1), (1, -2), (-1, -2), (-2, -1)]  # 状态空间，8个方向

entry = (2, 2)  # 出发地

x = [None] * (n * n)  # 一个解，长度固定64，形如[(2,2),(4,3),...]
X = []  # 一组解


# 冲突检测
def conflict(k):
    global n, p, x, X

    # 步子 x[k] 超出边界
    if x[k][0] < 0 or x[k][0] >= n or x[k][1] < 0 or x[k][1] >= n:
        return True

    # 步子 x[k] 已经走过
    if x[k] in x[:k]:
        return True

    return False  # 无冲突


# 回溯法（递归版本）
def subsets(k):  # 到达第k个元素
    global n, p, x, X

    if k == n * n:  # 超出最尾的元素
        print(x)
        # X.append(x[:]) # 保存（一个解）
    else:
        for i in p:  # 遍历元素 x[k-1] 的状态空间: 8个方向
            x[k] = (x[k - 1][0] + i[0], x[k - 1][1] + i[1])
            if not conflict(k):  # 剪枝
                subsets(k + 1)


# 测试
x[0] = entry  # 入口
subsets(1)  # 开始走第k=1步