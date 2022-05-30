class User:
    def __init__(self, username, passward):
        self.username = username
        self.passward = passward
        print("解释器调用__init__方法，初始化对象")

    def __new__(cls, usrname, passward):
        print("User类的对象开始创建!")
        return object.__new__(cls)

    def __str__(self):
        return "用户名%s, 密码%s" % (self.username, self.passward)

u = User('liang', '666')
print(u)