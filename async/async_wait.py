import asyncio


async def async_sleep(duration):
    await asyncio.sleep(duration)
    return duration


async def main():
    pending = set()
    for i in range(10):
        pending.add(asyncio.create_task(async_sleep(i+1)))

    while len(pending) > 0:
        done, pending = await asyncio.wait(pending, return_when='ALL_COMPLETED')
        print('len done:', len(done))
        for done_task in done:
            print(await done_task)

        # pending.add(asyncio.create_task(async_sleep(1)))

        print('len pending:', len(pending))
        print('*' * 10)


if __name__ == '__main__':
    asyncio.run(main())
