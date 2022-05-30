"""
效率:平均O(nlogn)

原理：
从数列中随机挑选出一个数作为基数；
重新排列数列，使得比基数小的元素在左边，比基数大元素在右边，相等的元素放左边或者右边都可以，最后使得该基数在处于数列中间位置，这个称为分区操作；
"""

def quick_sort(data, left, right):
    """快速排序

    :param data: 待排序的数据列表
    :param left: 基准数左边元素的索引
    :param right: 基准数右边元素的索引
    :return:
    """
    if left < right:
        mid = partition(data, left, right)  # 分区操作,mid代表基数所在的索引
        quick_sort(data, left, mid - 1)  # 对基准数前面进行排序
        quick_sort(data, mid + 1, right)  # 对基准数后面进行排序


def partition(data, left, right):
    tmp = data[left]  # 随机选择的基准数,从最左边开始选
    while left < right:
        while left < right and data[right] >= tmp:  # 右边的数比基准数大
            right -= 1  # 保留该数，然后索引指针往左移动
        data[left] = data[right]  # 否则此时右边数比基数小，则将该数放到基准位置
        while left < right and data[left] <= tmp:  # 右边的数比基准数小
            left += 1  # 此时保持该数位置不动，索引指针往前移动
        data[right] = data[left]  # 否则此时左边的数比基数大，则将该数放到右边
        print(data)
    data[left] = tmp  # 最后将基准数量放回中间
    return left  # 返回基准数位置


if __name__ == '__main__':
    data_list = [3, 7, 4, 7, 6, 8, 12, 2]
    print(data_list)
    quick_sort(data_list, 0, len(data_list)-1)
