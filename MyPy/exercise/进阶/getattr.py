"""测试属性不存在时捕获：__getattr__()"""
class Student:
    def __init__(self):
        self.name = 'Lucy'

    def __getattr__(self, item):  # 在获取不存在的属性时调用
        if item == 'score':
            return 99

print(Student().score)
