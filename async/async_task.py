import asyncio


async def async_sleep():
    print('before sleep')
    await asyncio.sleep(3)
    print(f'after sleep')


async def print_hello():
    print('hello')


async def main():
    task = asyncio.create_task(async_sleep())
    await async_sleep()
    await task
    await print_hello()


asyncio.run(main())
