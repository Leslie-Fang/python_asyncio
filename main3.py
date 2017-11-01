import time
import asyncio

now = lambda: time.time()

async def do_some_work(x):
    print('Waiting: ', x)
    # await asyncio.sleep(2)
    await do_work_first()
    return 'Done after {}s'.format(x)

async def do_work_first():
    print("The work need to be done at first place.")
    time.sleep(2)
    return 1

def callback(future):
    print('Callback: ', future.result())#future.result() is what's the task(coroutine) returns

async def do_work_second_loop():
    print("The work need to be done in second loop.")
    time.sleep(2)
    return 1

def callback2(future):
    print('Callback2: ', future.result())#future.result() is what's the task(coroutine) returns

start = now()

task = asyncio.ensure_future(do_some_work(2))
task.add_done_callback(callback)

pending = asyncio.Task.all_tasks()
loop = asyncio.get_event_loop()
# add the callback function
loop.run_until_complete(asyncio.gather(*pending))

# # task2 = asyncio.ensure_future(do_work_second_loop())
# pending = asyncio.Task.all_tasks()
# loop = asyncio.get_event_loop()
try:
    while 1:
        futus = asyncio.gather(do_work_second_loop())
        futus.add_done_callback(callback2)

        loop.run_until_complete(futus)
        time.sleep(2)
finally:
    loop.close()

print('TIME: ', now() - start)
