def fun():
    print('fun() is running.')
f = fun
f()  # 函数是对象，可以调用
# def log(func):
#     def wrapper(*args, **kwargs):  # 这里跳过不执行，到最后一句 return 才执行
#         print('call %s()' % func.__name__)
#         return func(*args, **kwargs)
#     return wrapper
#
# @log  # @log 放在函数定义出相当于执行了: test = log(test)
# def test():
#     print('test() is running.')

# test()

# def log(text):
#     def decorator(func):
#         def wrapper(*args, **kwargs):
#             print('%s %s():' % (text, func.__name__))
#             return func(*args, **kwargs)
#         return wrapper
#     return decorator
#
# @log('execute')  # log('execute')(now)
# def test():
#     print('test() is running.')
#
# test()

import functools
def log(text):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            print('%s %s():' % text, func.__name__)
            return func(*args, **kwargs)
        return wrapper
    return decorator
