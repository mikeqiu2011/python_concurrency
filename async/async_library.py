import asyncio
import time
import requests


async def get_url_response(url, loop):
    resp = await loop.run_in_executor(None, requests.get, url)
    return resp.text


async def main():
    urls = ['https://google.com',
            'https://python.org',
            'https://www.apple.com',
            'https://medium.com',]

    start = time.time()
    sync_text_reponse = []

    for url in urls:
        sync_text_reponse.append(requests.get(url).text)

    print(f'sync requests took {time.time() - start}')

    start = time.time()
    tasks = []
    loop = asyncio.get_event_loop()

    for url in urls:
        tasks.append(asyncio.create_task(get_url_response(url, loop)))

    async_text_response = await asyncio.gather(*tasks)
    print(async_text_response)

    print(f'ASYNC requests took {time.time() - start}')


if __name__ == '__main__':
    asyncio.run(main())
