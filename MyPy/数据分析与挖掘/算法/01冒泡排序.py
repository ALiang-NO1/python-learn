"""
效率：O(n2)

原理：
比较相邻的元素，如果第一个比第二个大，就交换他们两个；
对每一对相邻元素做同样的工作，从开始第一对到结尾的最后一对。做完以后，最后的元素会是最大的数，这里可以理解为走了一趟；
针对所有的元素重复以上的步骤，除了最后一个；
持续每次对越来越少的元素重复上面的步骤，直到没有任何一对数字需要比较，最后数列就是从大到小一次排列；

优化版本：当某一趟走完以后发现并没有进行数据交换，那么此时的数列已经排列好了，
没有必要在进行下去。例如：极端情况下，数列本来已经排序好的，我们只需要走一趟即可完成排序。
"""


def bubble_sort(data):
    """
    冒泡排序优化版

    :param data:
    :return:
    """
    for i in range(len(data) - 1):  # 趟数
        exchange = False  # 交换标志
        for j in range(len(data) - i - 1):  # 遍历数据，依次交换
            if data[j] > data[j + 1]:  # 当较大数在前面
                data[j], data[j + 1] = data[j + 1], data[j]  # 交换两个数的位置
                exchange = True  # 改变标志
            print(data_list)
        if not exchange:  # 如果某一趟没有进行交换，代表排序完成
            print('已经是有序的了。')
            break


if __name__ == '__main__':
    import random

    data_list = list(range(7))
    random.shuffle(data_list)
    print(data_list)
    bubble_sort(data_list)
