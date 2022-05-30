def fn(first_name,last_name):
    """返回简洁的名字"""
    full_name = first_name+' '+last_name
    return full_name.title()
while True:
    print("\nPlease tell me your name.（Entet 'q' at any time to quit！）")
    f_name = input("Please tell me your first name:\n")
    if f_name == 'q':
        break
    l_name = input("Please tell me your last name:\n")
    if l_name == 'q':
        break
    fm_n = fn(f_name,l_name)
    print("Welcome! "+fm_n+"!")
