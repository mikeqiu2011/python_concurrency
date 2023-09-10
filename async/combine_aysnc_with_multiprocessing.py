import asyncio
import multiprocessing


class MultiprocessingAsync(multiprocessing.Process):
    def __init__(self, durations):
        super(MultiprocessingAsync, self).__init__()
        self._durations = durations

    async def async_sleep(self, duration):
        await asyncio.sleep(duration)
        return duration

    async def consecutive_sleep(self):
        pending = set()
        for duration in self._durations:
            pending.add(asyncio.create_task(self.async_sleep(duration)))

        while len(pending) > 0:
            done, pending = await asyncio.wait(pending, return_when='FIRST_COMPLETED')
            for done_task in done:
                print(await done_task)

    def run(self) -> None:
        asyncio.run(self.consecutive_sleep())
        print('Process finished')


if __name__ == '__main__':
    processes = []
    for i in range(2):
        p = MultiprocessingAsync(range(i*5, (i+1)*5))
        p.start()
        processes.append(p)

    for process in processes:
        process.join()


