import asyncio
import random

async def wait_random(max_delay=10):

    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay

def task_wait_random(max_delay):
    return asyncio.Task(wait_random(max_delay))

async def task_kwait_n(n, max_delay):
    delays = []

    tasks = [wait_random(max_delay) for _ in range(n)]

    for task in asyncio.as_completed(tasks):
        delay = await task
        delays.append(delay)

    return delays