#!/usr/bin/env python
# -*- coding:utf-8 -*-
def little_heap_sort(elems):
    def siftdown(elems, e, begin, end):
        i, j = begin, begin*2+1
        while j < end:
            if j+1 < end and elems[j] > elems[j+1]:
                j += 1
            if e < elems[j]:
                break
            elems[i] = elems[j]
            i, j = j, j*2 + 1
        elems[i] = e

    #构建小堆序   O(n)
    end = len(elems)
    for i in range(end//2, -1, -1):
        siftdown(elems, elems[i], i, end)

    #弹出堆顶元素放在末尾  O(nlogn)
    for i in range(end-1, 0, -1):       #O(n)
        e = elems[i]
        elems[i] = elems[0]
        siftdown(elems, e, 0, i)        #O(logn)



# 堆排序：因为队列里的元素是不满足大堆序的，所以首先要构建大堆序
# 构建完大堆序后，从堆顶弹出元素（该元素最大）并将其放在堆的末尾；以此循环执行
# 最终形成从大到小排序的队列
def big_head_sort(elems):
    def siftdown(elems, e, begin, end):
        i, j = begin, begin*2 + 1
        while j < end:
            if j+1 < end and elems[j]<elems[j+1]:
                j += 1
            if e > elems[j]:
                break
            elems[i] = elems[j]
            i, j = j, j*2 + 1
        elems[i] = e

    #构建大堆序 O(n)
    end = len(elems)
    for i in range(end//2, -1, -1):
        siftdown(elems, elems[i], i, end)

    #弹出堆顶元素放在末尾 O(nlogn)
    for i in range(end-1, 0, -1):
        e = elems[i]
        elems[i] = elems[0]
        siftdown(elems, e, 0, i)

if __name__=="__main__":
    l = [1,6,2,9,8,0,3,5,4,7]
    little_heap_sort(l)
    print(l)
    #[9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
    big_head_sort(l)
    print(l)
    #[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]