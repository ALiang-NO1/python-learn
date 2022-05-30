# 用散列表实现图的关系
graph = {}
graph["start"] = {}
graph["start"]["a"] = 6
graph["start"]["b"] = 2
graph["a"] = {}
graph["a"]["end"] = 1
graph["b"] = {}
graph["b"]["a"] = 3
graph["b"]["end"] = 5
graph["end"] = {}

# 创建节点的开销表，开销是指从start到该节点的权重
# 无穷大 
infinity = float("inf")
costs = {}
costs["a"] = 6
costs["b"] = 2
costs["end"] = infinity

# 父节点散列表
parents = {}
parents["a"] = "start"
parents["b"] = "start"
parents["end"] = None

# 已经处理过的节点，需要记录
processed = []


# 找到开销最小的节点
def find_lowest_cost_node(costs):
    # 初始化数据
    lowest_cost = infinity
    lowest_cost_node = None
    # 遍历所有节点
    for node in costs:
        # 该节点没有被处理
        if not node in processed:
            # 如果当前节点的开销比已经存在的开销小，则更新该节点为开销最小的节点
            if costs[node] < lowest_cost:
                lowest_cost = costs[node]
                lowest_cost_node = node
    return lowest_cost_node


# 找到最短路径
def find_shortest_path():
    node = "end"
    shortest_path = ["end"]
    while parents[node] != "start":
        shortest_path.append(parents[node])
        node = parents[node]
    shortest_path.append("start")
    return shortest_path


# 寻找加权的最短路径
def dijkstra():
    # 查询到目前开销最小的节点
    node = find_lowest_cost_node(costs)
    # 只要有开销最小的节点就循环
    while node is not None:
        # 获取该节点当前开销
        cost = costs[node]
        # 获取该节点相邻的节点
        neighbors = graph[node]
        # 遍历这些相邻节点
        for n in neighbors:
            # 计算经过当前节点到达相邻结点的开销,即当前节点的开销加上当前节点到相邻节点的开销
            new_cost = cost + neighbors[n]
            # 如果计算获得的开销比原本该节点的开销小，更新该节点的开销和父节点
            if new_cost < costs[n]:
                costs[n] = new_cost
                parents[n] = node
        # 遍历完毕该节点的所有相邻节点，说明该节点已经处理完毕
        processed.append(node)
        # 去查找下一个开销最小的节点，若存在则继续执行循环，若不存在结束循环
        node = find_lowest_cost_node(costs)
    # 循环完毕说明所有节点都已经处理完毕
    shortest_path = find_shortest_path()
    shortest_path.reverse()
    print(shortest_path)


# 测试
dijkstra()
