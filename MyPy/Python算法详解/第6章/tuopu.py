# -*- coding:utf8 -*-
import copy
import bisect

class Graph(object):

    def __init__(self, *args, **kwargs):
        self.node_neighbors = {}
        self.visited = {}
        self.edge_properties = {}  # 记录边的权重
        self.in_degree = {}  # 入度

    def add_nodes(self, nodelist):
        for node in nodelist:
            self.add_node(node)

    def add_node(self, node):
        if not node in self.node_neighbors:
            self.node_neighbors[node] = []

    def add_edge(self, edge, weight=1):
        u, v = edge
        if (v not in self.node_neighbors[u]) and (u not in self.node_neighbors[v]):
            self.node_neighbors[u].append(v)
            if (u != v):
                self.node_neighbors[v].append(u)
                self.edge_properties[edge] = weight
                self.edge_properties[(v, u)] = weight

    def add_arc(self, edge, weight=1):

        """ 加弧，有向"""
        u, v = edge
        if v not in self.node_neighbors[u]:
            self.node_neighbors[u].append(v)
            self.edge_properties[edge] = weight
            if v in self.in_degree:
                self.in_degree[v] = self.in_degree[v] + 1
            else:
                self.in_degree[v] = 1
            if u not in self.in_degree:
                self.in_degree[u] = 0

    def edge_weight(self, edge):
        if edge in self.edge_properties:
            return self.edge_properties[edge]
        return -1

    def nodes(self):
        return self.node_neighbors.keys()

    def depth_first_search(self, root=None):
        order = []

        def dfs(node):
            self.visited[node] = True
            order.append(node)
            for n in self.node_neighbors[node]:
                if not n in self.visited:
                    dfs(n)

        if root:
            dfs(root)
        for node in self.nodes():
            if not node in self.visited:
                dfs(node)
        print(order)
        return order

    def breadth_first_search(self, root=None):
        queue = []
        order = []

        def bfs():
            while len(queue) > 0:
                node = queue.pop(0)
                self.visited[node] = True
                for n in self.node_neighbors[node]:
                    if (not n in self.visited) and (not n in queue):
                        queue.append(n)
                        order.append(n)

        if root:
            queue.append(root)
            order.append(root)
            bfs()
        for node in self.nodes():
            if not node in self.visited:
                queue.append(node)
                order.append(node)
                bfs()
        print(order)

        return order

    def prim_min_tree(self, root=None):
        """最小生成树：普里姆算法"""
        spanning_tree = {}

        def light_edge():
            min_weight = 10000
            edge = None
            for node in self.visited.keys():
                for other in self.node_neighbors[node]:
                    if not other in self.visited:
                        if self.edge_weight((node, other)) != -1 and self.edge_weight((node, other)) < min_weight:
                            min_weight = self.edge_weight((node, other))
                            edge = (node, other)
            return edge, min_weight

        def get_unvisited_node():
            for node in self.nodes():
                if not node in self.visited:
                    return node

        while len(self.visited.keys()) != len(self.nodes()):
            edge, min_weight = light_edge()
            if edge:
                spanning_tree[(edge[0], edge[1])] = min_weight
                self.visited[edge[1]] = True
            else:
                node = root if root else get_unvisited_node()
                if node:
                    self.visited[node] = True
        return spanning_tree

    def topological_sorting(self):
        """拓扑序列的逆序列:找到入度为0的，取出，删除以Ta为开始的边，重复这样操作"""
        in_degree = copy.deepcopy(self.in_degree)
        order = []

        def find_zero_in_degree_node():
            for k, v in in_degree.items():
                if v == 0 and (not k in self.visited):
                    return k
            return None

        def do(node):
            self.visited[node] = True
            order.append(node)
            for other in self.node_neighbors[node]:
                if other not in self.visited:
                    in_degree[other] -= 1

        node = find_zero_in_degree_node()
        while node:
            do(node)
            node = find_zero_in_degree_node()
        if len(order) == len(self.nodes()):
            return order
        return None  # 有回环，没有拓扑序列

    def shortest_path(self, source):
        """最短路径Dijkstra's algorithm:O（n2）"""
        dist = {source: 0}  # 记录最终值
        q = [(0, source)]  # 记录source到点的距离
        while len(q) > 0:
            du, node = q.pop(0)
            self.visited[node] = True
            for n in self.node_neighbors[node]:
                if not n in self.visited:  # 如果还没有访问
                    alt = du + self.edge_properties[(node, n)]
                    if (not n in dist) or alt < dist[n]:
                        dist[n] = alt
                        bisect.insort(q, (alt, n))
        return dist  # 返回source到点的距离（如果不能到点，则没有值）


if __name__ == '__main__':
    g = Graph()
    g.add_nodes([i + 1 for i in range(6)])
    g.add_edge((1, 2), 6)
    g.add_edge((1, 3), 1)
    g.add_edge((1, 4), 5)
    g.add_edge((2, 3), 3)
    g.add_edge((2, 5), 5)
    g.add_edge((3, 4), 5)
    g.add_edge((3, 5), 6)
    g.add_edge((3, 6), 4)
    g.add_edge((4, 6), 2)
    g.add_edge((5, 6), 6)

    # print "nodes:", g.nodes()
    # order = g.depth_first_search(1)
    # order = g.breadth_first_search(1)
    # print "breadth_first_search", order, spanning_tree
    print("最小生成树", g.prim_min_tree(1))

    g2 = Graph()
    g2.add_nodes([i + 1 for i in range(6)])
    g2.add_arc((1, 2))
    g2.add_arc((1, 3))
    g2.add_arc((1, 4))
    g2.add_arc((3, 2))
    g2.add_arc((3, 5))
    g2.add_arc((6, 5))
    g2.add_arc((6, 4))
    g2.add_arc((4, 5))
    print("topological_sorting:", g2.topological_sorting())

    g3 = Graph()
    g3.add_nodes([i for i in range(6)])
    g3.add_arc((0, 2), 10)
    g3.add_arc((0, 4), 30)
    g3.add_arc((0, 5), 100)
    g3.add_arc((1, 2), 5)
    g3.add_arc((2, 3), 50)
    g3.add_arc((3, 5), 10)
    g3.add_arc((4, 3), 20)
    g3.add_arc((4, 5), 60)
    print("最短路径(到哪个点，距离)：", g3.shortest_path(0))
