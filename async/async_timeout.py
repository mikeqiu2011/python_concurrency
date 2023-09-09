import asyncio
import time


async def async_sleep(n):
    print('before sleep', n)
    await asyncio.sleep(3)
    print(f'after sleep', n)


async def print_hello():
    print('hello')


async def main():
    start = time.time()

    try:
        await asyncio.gather(
            asyncio.wait_for(async_sleep(30), 5),
            async_sleep(2),
            print_hello())
    except asyncio.TimeoutError:
        print('Encountered timeout error')

    print(f'it took {time.time() - start}')


asyncio.run(main())
