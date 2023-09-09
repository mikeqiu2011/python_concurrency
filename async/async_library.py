import asyncio
import time
import requests


async def main():
    urls = ['https://google.com',
            'https://python.org',
            'https://www.apple.com',
            'https://medium.com',
            'https://xiaobaotv.net/index.php']

    start = time.time()

    for url in urls:
        requests.get(url)

    print(f'it took {time.time() - start}')


if __name__ == '__main__':
    asyncio.run(main())
