class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def say_age(self):
        print(self.name, "的年龄是", self.age)

class Student(Person):
    def __init__(self, name, age, score):
        Person.__init__(self, name, age)
        self.__score = score

    def say_score(self):
        print('{0}的分数是{1}'.format(self.name, self.__score))

s1 = Student('晾', 18, 120)
s1.say_age()
print(s1._Student__score)
s1.say_score()