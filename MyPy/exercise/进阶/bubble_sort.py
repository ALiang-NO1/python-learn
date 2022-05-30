def bubble_sorted(list):
    n = len(list)
    count = 0
    for k in range(n-2):  # k:[0,3]
        for i in range(n-1-k):  # i:[0,3-k]
            if list[i] > list[i+1]:
                list[i], list[i+1] = list[i+1], list[i]
            count += 1
        if count == 0:
            break
    print(list)

bubble_sorted([6, 3, 5, 12, 8, 7, 21, 13])