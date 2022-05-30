def prime(num):
    if 2 == num:
        return True
    for i in range(2, num):
        if num % i == 0:
            return False
    else:
        return True
