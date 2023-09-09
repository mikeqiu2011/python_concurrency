import asyncio


async def async_sleep():
    await asyncio.sleep(3)
    print(f'sleep went well')


async def print_hello():
    print('hello')


async def main():
    await async_sleep()
    await print_hello()


asyncio.run(main())
