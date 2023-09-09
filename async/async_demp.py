import asyncio


async def async_sleep():
    await asyncio.sleep(3)
    print(f'sleep went well')


asyncio.run(async_sleep())
