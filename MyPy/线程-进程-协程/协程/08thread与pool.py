import time, asyncio

def func():
    time.sleep(1)
    return 'SB'

async def main():
    loop = asyncio.get_event_loop()

    print("------Run in default executor----------")
    fut = loop.run_in_executor(None, func)
    result = await fut

    # print("------Run in custom threadpool----------")
    # with concurrent.futures.ThreadPoolExecutor() as pool:
    #     result = await loop.run_in_executor(None, func())

    # print("------Run in default executor----------")
    # with concurrent.futures.ProcessPoolExecutor() as pool:
    #     result = await loop.run_in_executor(None, func())

    print(result)
