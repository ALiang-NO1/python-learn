import pandas as pd
import numpy as np
import random
import matplotlib.pyplot as plt

'''
用蒙特卡罗方法，验证凯利公式的计算得到资金比例是不是最佳的
'''

pwin = 0.6  # 胜率
b = 1  # 净赔率


# 凯利值
def kelly(pwin, b):
    '''
    参数
        pwin 胜率
        b    净赔率
    返回
        f    投注资金比例
    '''
    f = (b * pwin + pwin - 1) / b
    return f


# 游戏
def play_game(f, cash=100, m=100):
    global pwin, b

    res = [cash]
    for i in range(m):
        if random.random() <= pwin:
            res.append(res[-1] + int(f * res[-1]) * b)
        else:
            res.append(res[-1] - int(f * res[-1]))
    return res


# 蒙特卡罗方法重复玩游戏
def montecarlo(n=1000, f=0.15, cash=1000, m=100):
    res = []

    for i in range(n):
        res.append(play_game(f, cash, m))

    # return pd.DataFrame(res).sum(axis=0) / n   #【 数学期望】不平滑
    return np.exp(np.log(pd.DataFrame(res)).sum(axis=0) / n)  # 【几何期望】平滑


n = 1000  # 重复次数
cash = 1000  # 初始资金池
m = 100  # 期数

f = 0.1  # 资金比例 10%
res1 = montecarlo(n, f, cash, m)

fk = kelly(pwin, b)  # 资金比例 凯利值
res2 = montecarlo(n, fk, cash, m)

f = 0.5  # 资金比例 50%
res3 = montecarlo(n, f, cash, m)

f = 1.0  # 资金比例 100%
res4 = montecarlo(n, f, cash, m)

# 画个图看看
fig = plt.figure()
axes = fig.add_subplot(111)

axes.plot(res1, 'r-', label='10%')
axes.plot(res2, 'g*', label='{:.1%}'.format(fk))
axes.plot(res3, 'b-', label='50%')
axes.plot(res4, 'k-', label='100%')
plt.legend(loc=0)

plt.show()