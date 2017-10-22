import asyncio
import time

now = lambda: time.time()

async def myAwait(x):
    print("In await; Before sleep")
    time.sleep(x)
    print("In await; After sleep")

async def do_some_work(x):
    print('Waiting: ', x)
    #await asyncio.sleep(x)
    await myAwait(x)
    return 'Done after {}s'.format(x)


start = now()

coroutine = do_some_work(2)
loop = asyncio.get_event_loop()
task = asyncio.ensure_future(coroutine)
loop.run_until_complete(task)

print('Task ret: ', task.result())
print('TIME: ', now() - start)