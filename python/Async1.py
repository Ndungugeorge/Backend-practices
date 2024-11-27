import asyncio
async def hello():
    print ("hello!")
    await asyncio.sleep(1)
    print ("hello again")

asyncio.run(hello())