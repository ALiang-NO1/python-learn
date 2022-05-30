import asyncio

# async def fun():
#     print("开始...")
#     await asyncio.sleep(1)
#     print("结束！")
# asyncio.run(fun())

async def others():
    print("start...")
    await asyncio.sleep(1)
    print("end!")
    return "返回值"
# r = asyncio.run(others())
# print(r)

async def func():
    print("执行协程内部代码")
    response = await(others())
    print("IO请求结果为：", response)

async def main():
    print("main开始！....")
    task1 = asyncio.create_task(func())
    task2 = asyncio.create_task(func())
    ret1 = await task1
    ret2 = await task2
    # task_list = [task1, task2]
    # await asyncio.wait(task_list)
    print(ret1, ret2)
    print("main结束！")

asyncio.run(main())