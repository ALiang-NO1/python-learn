import asyncio

def callback_func(task):
    print("函数执行结果：", task.result())  # result()返回主函数return值

async def request(url):
    print("正在请求：", url)
    await asyncio.sleep(2)
    print("请求成功：", url)

c = request('www.baidu.com')
loop = asyncio.get_event_loop()  # 创建事件循环对象
print('loop:', loop)

# task = loop.create_task(c)    # 低级
task = asyncio.ensure_future(c)  # 低级
print('task', task)

task.add_done_callback(callback_func)
loop.run_until_complete(task)   # 注册并启动协程
print(5/2)
