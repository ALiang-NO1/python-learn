class Itcast(object):
    def __init__(self, subject1):
        self.subject1 = subject1
        self.subject2 = "java"

    def __getattribute__(self, obj):  # 重写父类的__getattribute__方法，形参obj是访问的属性，是一个属性名字字符串
        print("obj------>%s" % obj)
        if obj == "subject1":  # 如果属性名是subject1，可以做一些操作
            print("获取subject1的值：")
            return "python"  # 不能return self. 否则self.与getattribute同时进行，程序死掉
        else:  # else必须写，如果不写，那subject2以及show方法就访问不到了
            temp = object.__getattribute__(self, obj)  # 调用父类的__getattribute__方法
            print("获取其他属性的值：")
            return temp  # 不写return的话，show方法无法执行

    def show(self):
        print("show（）方法执行！")

s = Itcast("python")
print(s.subject1)
print(s.subject2)
s.show()  # show方法执行的时候也会先走属性拦截器方法
