import random
import asyncio

async def async_generator():
    for _ in range (10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)

#asyncio.run(async_generator())


async def print_yielded_values():
   # result = []
    async for i in async_generator():
       #result.append(i)
        print(i)

asyncio.run(print_yielded_values())