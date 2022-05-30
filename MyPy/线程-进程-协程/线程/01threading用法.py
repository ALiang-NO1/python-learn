import threading
import time

def test():
    for i in range(2):
        time.sleep(1)   # 设置一个等待时间
        print('线程名字：%s' % threading.current_thread().name)

if __name__ == '__main__':
    my_list = []
    for i in range(5):
        a = threading.Thread(target=test)
        my_list.append(a)
    for j in my_list:
        j.start()
        j.join()
    # for m in my_list:
    #     m.join()