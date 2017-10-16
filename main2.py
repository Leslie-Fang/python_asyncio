import asyncio
import time

async def do_some_work(x):
    '''
    with the async directivate, we would define a coroutine
    when call this function, it would not be implemented, but return a coroutine object
    the coroutine object need to be registered into the loop
    '''
    print('Waiting: ', x)

if __name__ == "__main__":
    print("Hello world!")
    now = lambda : time.time()
    start = now()
    #create a coroutine object
    coroutine = do_some_work(2)
    #create a loop
    loop = asyncio.get_event_loop()
    #use the coroutine object to create a task
    #asyncio.ensure_future(coroutine) and loop.create_task(coroutine), both could be used to create the task
    task =loop.create_task(coroutine)
    print(task)#should be pending state
    #add the coroutine object into the loop, and start the loop
    loop.run_until_complete(task)
    print(task)  # should be finished state
    print('TIME: ', now() - start)


