from datetime import datetime
import trio
import httpx
import requests



class Task:
    def __init__(self):
        trio.run(self.http)
        self.clent2()


    async def http(self):
        async with trio.open_nursery() as nursery:
            nursery.start_soon(self.clent1)
 


    async def clent1(self):
        print("httpx测试。。。。")
        async with httpx.AsyncClient() as client:  # 创建一个异步client
            # 1/0
            r = await client.get('https://www.example.com/')
            print(r)
            print(datetime.now())
            print(r.text)


    def clent2(self):
        print("requests测试。。。。")
        r =  requests.get('https://www.example.com/')
       
        print(r)
        print( r.text)


