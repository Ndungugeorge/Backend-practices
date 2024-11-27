import asyncio
import random

async def task1():
    delay = random.randint(1, 5)
    print("Wait for {} seconds".format(delay))
    await asyncio.sleep(delay)
    print("Am done executing with {} seconds".format(delay))

async def main():
    await asyncio.gather(task1(), task1())

asyncio.run(main())