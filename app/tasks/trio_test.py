from datetime import datetime
import httpx
from datetime import datetime


async def test():

    async with httpx.AsyncClient() as client:  # 创建一个异步client
        try:
            # 1/0
            r = await client.get('https://www.example.com/')
            print(r)
            print(datetime.now())
        except Exception as e:
            print(str(e))






# trio.run(main)