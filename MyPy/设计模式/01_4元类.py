# class MyInt(type):
#     def __call__(cls, *args, **kwargs):
#         print('args:', args)
#         return type.__call__(cls, *args, **kwargs)
#
#
# class Int(metaclass=MyInt):
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
#
# i = Int(1, 2)


class MetaSingleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(MetaSingleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class Logger(metaclass=MetaSingleton):
    pass


logger = Logger()
logger2 = Logger()
print(logger)
print(logger2)

# 单例模式1：在数据库上的应用
import sqlite3


class Database(metaclass=MetaSingleton):
    con = None

    def __init__(self):
        if self.con is None:
            self.con = sqlite3.connect('db.sqlit3')
            self.cur = self.con.cursor()
            return self.cur


db = Database()
db2 = Database()
print(db)
print(db2)
