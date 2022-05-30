def heron(a,b,c):
    """输入三角形三边求面积"""
    p = (a+b+c)/2
    a = p*(p-a)*(p-b)*(p-c)
    s = a**0.5
    print(s)
