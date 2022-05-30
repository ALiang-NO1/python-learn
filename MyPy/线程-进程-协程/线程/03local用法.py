import time
import threading

class Apple:
    def __init__(self):
        self.apple_number = 6    # 定义6个苹果，每个苹果有一个标号

    def get_apple_number(self):
        return self.apple_number

    def sell_apple(self):
        time.sleep(1)   # 当前线程休眠，会阻塞当前的线程，这个时间提供给用户付款，完成付款后执行售出操作
        print('第%d个苹果已卖' % self.apple_number)
        self.apple_number -= 1

ap = Apple()
local = threading.local()
def thread_one(name):
    global ap
    local.name = name
    student_name = local.name
    print("线程名：%s 学生姓名：%s" % (threading.current_thread().name, student_name))
    while True:
        query_apple_number = ap.get_apple_number()  # 查询是否还有苹果
        if query_apple_number > 0:  # 苹果数量大于0就执行一次出售操作
            ap.sell_apple()
        else:
            break

if __name__ == '__main__':
    apple_one = threading.Thread(target=thread_one, args=("张三",), name='Thread_A')
    apple_two = threading.Thread(target=thread_one, args=("李四",), name='Thread_B')
    apple_one.start()
    apple_two.start()
