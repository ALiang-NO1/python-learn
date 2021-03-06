"""
效率：O(n2)

原理：
以从小到大排序为例，元素0为第一个元素，插入排序是从元素1开始，尽可能插到前面。
插入时分插入位置和试探位置，元素i的初始插入位置为i，试探位置为i-1，在插入元素i时，依次与i-1,i-2······元素比较，
如果被试探位置的元素比插入元素大，那么被试探元素后移一位，元素i插入位置前移1位，直到被试探元素小于插入元素或者插入元素位于第一位。
重复上述步骤，最后完成排序
"""

def insert_sort(data):
    for i in range(1, len(data)):
        j = i
        while j > 0:
            if data[j] < data[j-1]:
                data[j], data[j-1] = data[j-1], data[j]
            j -= 1
        print(data)


if __name__ == '__main__':
    data_list = [3, 7, 4, 7, 6]
    print(data_list)
    insert_sort(data_list)