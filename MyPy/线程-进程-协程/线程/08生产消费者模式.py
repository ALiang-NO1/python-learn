import time
import threading
from queue import Queue

class Producer(threading.Thread):
    def run(self):
        global queue
        count = 0
        while True:
            if queue.qsize() < 1000:
                for i in range(100):
                    count += 1
                    msg = "成品" + str(count)
                    queue.put(msg)
                time.sleep(0.5)
class Consumer(threading.Thread):
    def run(self):
        global queue
        count = 0
        while True:
            if queue.qsize() > 100:
                for i in range(3):
                    count -= 1
                    msg = self.name + "消费了" + queue.get()
                    print(msg)
                time.sleep(1)
if __name__ == '__main__':
    queue = Queue()
    p = Producer()
    p.start()
    time.sleep(1)
    c = Consumer()
    c.start()