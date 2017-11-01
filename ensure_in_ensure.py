import asyncio
import time

async def task3(task):
    print("This is {}.".format(task))

async def task2(task):
    print("This is {}.".format(task))
    for item in range(5):
        asyncio.ensure_future(task3(task + str(item)))

async def task1():
    print("This is task1.")
    for item in range(5):
        asyncio.ensure_future(task2("task"+str(item)))
    pass

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    try:
        while 1:
            # loop tasks
            task_fetch_trades = asyncio.ensure_future(task1())
            pending = asyncio.Task.all_tasks()
            loop.run_until_complete(asyncio.gather(*pending))
            time.sleep(5)
    finally:
        loop.close()