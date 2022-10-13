from datetime import datetime
import trio
import httpx
from datetime import datetime


async def test():

    async with httpx.AsyncClient() as client:  # 创建一个异步client
        r = await client.get('https://www.example.com/')
        print(r)
        print(datetime.now())




async def main():
    async with trio.open_nursery() as nursery:
        nursery.start_soon(test)
        nursery.start_soon(test)
        nursery.start_soon(test)
        nursery.start_soon(test)
        nursery.start_soon(test)
        nursery.start_soon(test)
        nursery.start_soon(test)
        nursery.start_soon(test)

trio.run(main)