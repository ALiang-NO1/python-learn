"""  已知一个迷宫的出口，需要找到一个出口，如果存在这一的出路，输出它的路径。
     走迷宫的过程中呈九宫格方式，可以从上、下、左、右、左上、左下、右上和右下八个方向移动。"""
import pprint, copy
# 迷宫（1是墙，0是通路）
maze = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [0, 0, 1, 0, 1, 1, 1, 1, 0, 1],
        [1, 1, 0, 1, 0, 1, 1, 0, 1, 1],
        [1, 0, 1, 1, 1, 0, 0, 1, 1, 1],
        [1, 1, 1, 0, 0, 1, 1, 0, 1, 1],
        [1, 1, 0, 1, 1, 1, 1, 1, 0, 1],
        [1, 0, 1, 0, 0, 1, 1, 1, 1, 0],
        [1, 1, 1, 1, 1, 0, 1, 1, 1, 1]]
m, n = 8, 10  # 8行，10列
entry = (1, 0)  # 迷宫入口
path = [entry]  # 一个解（路径）
paths = []  # 一组解
# 移动的方向（顺时针8个：N, EN, E, ES, S, WS, W, WN）
directions = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]
# 冲突检测
def conflict(nx, ny):
    """首先进行一个冲突检测，判断当前路径是否处在迷宫当中，如果不越界就可以通行，然后套用子集数模板，定义函数来进行试探迷宫，如果当前坐标是出口，
    就保存下来，如果不是出口，遍历八个方向（八个状态），如果发生没有发生冲突检测就去除掉次坐标，然后出站，通过一次次试探最终找到出口，
    最后输出一个可视化的解来测试程序的正确性。"""
    global m, n, maze
    # 是否在迷宫中，以及是否可通行
    if 0 <= nx < m and 0 <= ny < n and maze[nx][ny] == 0:   #不越界，可以通行
        return False
    return True
# 套用子集树模板
def walk(x, y):  # 到达(x,y)格子
    global entry, m, n, maze, path, paths, directions
    if (x, y) != entry and (x % (m - 1) == 0 or y % (n - 1) == 0):  # 出口
        # print(path)
        paths.append(path[:])  # 直接保存，未做最优化
    else:
        for d in directions:  # 遍历8个方向(亦即8个状态)
            nx, ny = x + d[0], y + d[1]
            path.append((nx, ny))  # 保存，新坐标入栈
            if not conflict(nx, ny):  # 剪枝
                maze[nx][ny] = 2  # 标记，已访问
                walk(nx, ny)
                maze[nx][ny] = 0  # 回溯，恢复
            path.pop()  # 回溯，出栈
# 解的可视化（根据一个解x，复原迷宫路径，'2'表示通路）
def show(path):
    global maze
    maze2 = copy.deepcopy(maze)
    for p in path:
        maze2[p[0]][p[1]] = 2  # 通路
    pprint.pprint(maze)  # 原迷宫
    print()
    pprint.pprint(maze2)  # 带通路的迷宫
# 测试
walk(1, 0)
print(paths[-1], '\n')  # 看看最后一条路径
show(paths[-1])