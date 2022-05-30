"""
效率：O(n2)

原理：
每一次从待排序的列表中选出一个元素，并将其与其他数依次比较，若列表中的某个数比选中的数小，则交换位置，
把所有数比较完毕，则会选出最小的数，将其放在最左边（这一过程称为一趟）；
重复以上步骤，直到全部待排序的数据元素排完；
"""

def select_sort(data):
    """选择排序"""
    for i in range(len(data) - 1):  # 趟数
        min_index = i  # 记录i趟开始最小的数的索引，我们从最左边开始
        for j in range(i + 1, len(data)):  # 每一次趟需要循环的次数
            if data[j] < data[min_index]:  # 当数列中的某一个数比开始的数要小时候，更新最小值索引位置
                min_index = j
        data[i], data[min_index] = data[min_index], data[i]  # 一趟走完，交换最小值的位置，第一趟最小
        print(data)


if __name__ == '__main__':
    data_list = [3, 7, 4, 7, 6]
    print(data_list)
    select_sort(data_list)
