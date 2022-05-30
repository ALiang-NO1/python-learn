def recursive_mult(num1, num2, value):
    if num1 == 0 or num2 == 0:
        value += 0
    if num2 < 0:
        value -= num1
        num2 += 1
        value = recursive_mult(num1,num2,value)
    elif num2 > 0:
        value += num1
        num2 -= 1
        value = recursive_mult(num1,num2,value)
    return value


def main():
    num1 = int(input("input first number: "))
    num2 = int(input("input second number: "))
    value = 0
    value = recursive_mult(num1,num2,value)
    print(value)

if __name__ =='__main__':
    main()