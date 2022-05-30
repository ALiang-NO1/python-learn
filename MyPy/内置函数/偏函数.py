# 近代
def old_int2(int, base=2):
    """二进制转十进制"""
    return int(int, base)

# 现代
import functools
int2 = functools.partial(int, base=2)
print(int2('110'))

sum2 = functools.partial(sum, [1, 2, 3, 4])
print(sum2())