import asyncio


async def main():
    tasks = set()
    for i in range(10):
        tasks.add(asyncio.create_task(asyncio.sleep(i+1)))

    done, pending = await asyncio.wait(tasks)
    print(done)
    print(pending)


if __name__ == '__main__':
    asyncio.run(main())
