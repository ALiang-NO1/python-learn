def get_max(number):    # 寻最小值函数
    if len(number) == 1:
        return number[0]
    else:
        if number[1] > number[0]:
            return number[0]
        else:
            return number[1]
# 分治法
def solve(number):
    n = len(number)
    if n <= 2:  # 数据规模小于等于2使用get_max()函数
        return get_max(number)
    # 分解（子问题规模为 n/2）
    left_list, right_list = number[:n // 2], number[n // 2:]
    # 递归（树），分治
    left_max, right_max = solve(left_list), solve(right_list)
    # 合并
    return get_max([left_max, right_max])
if __name__ == "__main__":
    # 测试数据
    test_list = [33,52,2,25,63,75,43,72,45,97,53,25,14,18,3,5]
    # 求出最小值
    print(solve(test_list))