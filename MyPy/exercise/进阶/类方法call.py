class Student:
    def __init__(self, name):
        self.name = name

    def __call__(self, *args, **kwargs):
        print('My name is:', self.name)

s = Student('Liang')
print('s.Callable?', callable(s))
s()