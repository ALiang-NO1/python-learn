import time

##棋盘长宽
X = Y = 5

##马可以选择走的步数
STEP = 8
##马可以选择走的方式
nextList = [(2, -1), (2, 1), (1, 2), (-1, 2), (-2, 1), (-2, -1), (-1, -2), (1, -2)]  ##下左下逆时针

##出发点
startPoint=(2,0)

##初始化棋盘
chess=[[0 for j in range(Y)] for i in range(X)]



##打印棋盘
def printChess():
    for i in range(X):
        print(chess[i])
    print('over')

##判断下一步是否可走
def nextOk(point, i):
    nextp = (point[0] + nextList[i][0], point[1] + nextList[i][1])
    if 0 <= nextp[0] < X and 0 <= nextp[1] < Y and chess[nextp[0]][nextp[1]] == 0:
        return True, nextp
    else:
        return False, point

##获得下一步可走列表
def findNext(point):
    list = []
    for i in range(STEP):
        ok, pointn = nextOk(point, i)
        if ok:
            list.append(pointn)
    return list

##获得步数最少的下一步（贪婪算法）
def getBestNext(point, step):
    temp =X+1
    best = (-1, -1)

    list = findNext(point)
    lenp = len(list)
    for i in range(lenp):
        n = len(findNext(list[i]))
        if n < temp:
            if n > 0:
                temp = n
                best = list[i]
            elif n == 0 and step == X * Y:
                best = list[i]
    return best

##深度遍历 递归方式（速度很慢 对比方法）
def traverse(point, count):
    global sum_count
    if count > X * Y:
        return True
    for i in range(STEP):
        ok, nextp = nextOk(point, i)
        if ok:
            chess[nextp[0]][nextp[1]] = count
            result = traverse(nextp, count + 1)
            if result:
                return True
            else:
                chess[nextp[0]][nextp[1]] = 0
    return False

##迭代方式 贪婪算法
def traverseFast(point, step):
    chess[point[0]][point[1]] = step
    while 1:
        step += 1
        best = getBestNext(point, step)
        if best[0] == -1:
            return step
        else:
            chess[best[0]][best[1]] = step
            point = best
    return step

##测试递归方式
def testSlow():
    start = time.clock()
    chess[startPoint[0]][startPoint[1]]=1
    ok = traverse(startPoint,2)
    if ok:
        print('遍历成功')
    else:
        print('遍历失败')
    printChess()
    print('user_time==', time.clock() - start)

##测试贪婪算法
def testFast():
    start = time.clock()
    step = traverseFast(startPoint, 1)
    if step - 1 == X * Y:
        print('快速遍历成功')
    else:
        print('快速遍历失败')
    printChess()
    print('user_time==', time.clock() - start)

if __name__ == '__main__':
    testFast()
    chess = [[0 for j in range(Y)] for i in range(X)]
    testSlow()