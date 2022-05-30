class Person:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age
        self._job = 'stu'

    def _getName(self):
        print('The student names', self.__name)

    def __getAge(self):
        print(f'The student is {self.__age} years old.')

    def get_info(self, arg):
        if arg == 'name':
            self._getName()
        elif arg == 'age':
            self.__getAge()

t = Person('Liang', 23)
t.get_info('name')
t._getName()
print(t._job)
print('私有属性：' + t._Person__name)
