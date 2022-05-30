import threading
from threading import Event

"""面试题：有两个线程 A、B，A 线程打印 a,b,c 的字母，B线程打印 2,4,6 的数字，A、B 线程将轮询打印，如：a2 b4 c6..."""
# 打印字母函数
def printLetter(letterEvent, numEvent):  # （字母状态，数字状态）
    for item in ["a", "b", "c"]:
        letterEvent.wait()  # 等待字母的 Event() 变为 True
        print(item, end="")
        letterEvent.clear()  # 字母的 Event() 设为 False
        numEvent.set()  # 数字的 Event() 设为 True


# 打印数字函数
def printNum(numEvent, letterEvent):  # （数字状态，字母状态）
    for item in [2, 4, 6]:
        numEvent.wait()
        print(item, end=" ")
        numEvent.clear()
        letterEvent.set()


if __name__ == '__main__':
    letterEvent, numEvent = Event(), Event()
    t1 = threading.Thread(target=printLetter, args=(letterEvent, numEvent))
    t2 = threading.Thread(target=printNum, args=(numEvent, letterEvent))

    threads = []
    threads.append(t1)
    threads.append(t2)

    for t in threads:
        t.start()

    letterEvent.set()