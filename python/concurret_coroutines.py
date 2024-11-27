import asyncio

async def func1():
    print("Tast1 starting")
    await asyncio.sleep(2)
    print("task1 Done")

async def func2():
    print("Tast2 starting")
    await asyncio.sleep(1)
    print("task2 Done")

async def main():
    await asyncio.gather(func1(),func2())

asyncio.run(main())


