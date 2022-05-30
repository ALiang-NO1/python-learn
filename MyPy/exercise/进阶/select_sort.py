def select_sorted(list):
    n = len(list)
    for i in range(n-1):  # i:[0:3]
        min_index = i  # i
        for j in range(i+1, n):  # [i:4]
            if list[min_index] > list[j]:  # list[i]>list[j]--交换
                min_index = j
        if min_index != i:
            print(f'交换第{i}次: {list[i]}-{list[min_index]}')
            list[i], list[min_index] = list[min_index], list[i]
            print(list)
            print()
    print(list)

select_sorted([23, 3, 12, 27, 3])