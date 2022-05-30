def insert_list(L, i, element):
    L_lenght = len(L)
    if i < 1 or i > L_lenght:
        return False
    if i <= L_lenght:
        for k in range(i-1, L_lenght)[::-1]:
            L[k+1:k+2] = [L[k]]
        L[i-1] = element
    print(L)
    return True
L = [1,2,3,4]
insert_list(L, 2, 0)