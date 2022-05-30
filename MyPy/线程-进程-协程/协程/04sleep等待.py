import asyncio

@asyncio.coroutine
def hello():
    print('start....')
    # 当 asyncio.sleep()返回时，线程就可以从 yield from 拿到返回值（此处是 None），然后接着执行下一行语句
    yield from asyncio.sleep(4)
    print('end!')

loop = asyncio.get_event_loop()
tasks = [hello() for _ in range(5)]
loop.run_until_complete(asyncio.wait(tasks))
loop.close()
