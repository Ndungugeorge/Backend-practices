import asyncio
import random
import time

async def wait_random(max_delay=10):

    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay

async def wait_n(n, max_delay):
    delays = []

    tasks = [wait_random(max_delay) for _ in range(n)]

    for task in asyncio.as_completed(tasks):
        delay = await task
        delays.append(delay)

    return delays

async def measure_time(n, max_delay):
    start_time = time.perf_counter()

    await wait_n(n, max_delay)

    end_time = time.perf_counter()

    total_time = end_time - start_time
    return total_time / n


n = 5
max_delay = 9

print(asyncio.run(measure_time(n, max_delay)))
