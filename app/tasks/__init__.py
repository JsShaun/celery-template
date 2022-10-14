import trio
import httpx
from datetime import datetime



class Task:
    def __init__(self):
        trio.run(self.http)
        self.test()


    async def http(self):
        async with trio.open_nursery() as nursery:
            nursery.start_soon(self.clent)
            nursery.start_soon(self.clent)
            nursery.start_soon(self.clent)
            nursery.start_soon(self.clent)
            nursery.start_soon(self.clent)
            nursery.start_soon(self.clent)
            nursery.start_soon(self.clent)
            nursery.start_soon(self.clent)


    async def clent(self):
        try:
            async with httpx.AsyncClient() as client:  # 创建一个异步client
                # 1/0
                r = await client.get('https://www.example.com/')
                print(r)
                print(datetime.now())
        except Exception as e:
            print(str(e))

    def test(self):
        print("这里是测试。。。")


