import time
import asyncio

now = lambda: time.time()

async def do_some_work(x):
    print('Waiting: ', x)
    return 'Done after {}s'.format(x)

def callback(future):
    print('Callback: ', future.result())#future.result() is what's the task(coroutine) returns

start = now()

coroutine = do_some_work(2)
loop = asyncio.get_event_loop()
task = asyncio.ensure_future(coroutine)
# add the callback function
task.add_done_callback(callback)
loop.run_until_complete(task)

print('TIME: ', now() - start)
