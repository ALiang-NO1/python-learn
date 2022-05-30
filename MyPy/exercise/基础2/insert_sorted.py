def insert_sorted(list):
    n = len(list)
    for j in range(1, n):
        i = j
        while i > 0:
            if list[i] < list[i-1]:
                list[i], list[i-1] = list[i-1], list[i]
            else:
                break
            i -= 1
    print(list)

insert_sorted([14, 31, 23, 14, 19, 3])
