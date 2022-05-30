import threading
import asyncio

@asyncio.coroutine
def hello():
    print('Hello world! (%s)' % threading.current_thread())
    yield from asyncio.sleep(1)
    print('Hello world again! (%s)' % threading.current_thread())

loop = asyncio.get_event_loop()
tasks = [hello(), hello()]  # 两个 coroutine 是由同一个线程并发执行的
loop.run_until_complete(asyncio.wait(tasks))
loop.close()