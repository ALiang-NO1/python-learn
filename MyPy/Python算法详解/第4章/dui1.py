import heapq
h = []
#使用heappush()函数把一项值压入堆heap，同时维持堆的排序要求。
heapq.heappush(h, 5)
heapq.heappush(h, 2)
heapq.heappush(h, 8)
heapq.heappush(h, 4)
print(heapq.heappop(h))
heapq.heappush(h, 5)
#使用heapq.heappop(heap)
heapq.heappush(h, 2)
heapq.heappush(h, 8)
heapq.heappush(h, 4)
print(heapq.heappop(h))
print(heapq.heappop(h))
#使用heapq.heappushpop(heap, item)
h = []
heapq.heappush(h, 5)
heapq.heappush(h, 2)
heapq.heappush(h, 8)
print(heapq.heappushpop(h, 4))
#使用heapq.heapify(x)
h = [9, 8, 7, 6, 2, 4, 5]
heapq.heapify(h)
print(h)
#使用函数heapq.heapreplace(heap, item)
heapq.heapify(h)
print(heapq.heapreplace(h, 1))
print(h)
#使用heapq.merge(*iterables)
heapq.heapify(h)
l = [19, 11, 3, 15, 16]
heapq.heapify(l)
for i in heapq.merge(h,l):
    print(i, end = ',')
