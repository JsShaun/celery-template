from asyncinit import asyncinit
import trio
from . import trio_test



@asyncinit
class Task:
    async def __init__(self):
        await self.http()
    

    async def add(self,x, y):
        return x + y



    async def http(self):
        async with trio.open_nursery() as nursery:
            nursery.start_soon(trio_test.test)
            nursery.start_soon(trio_test.test)
            nursery.start_soon(trio_test.test)
            nursery.start_soon(trio_test.test)
            nursery.start_soon(trio_test.test)
            nursery.start_soon(trio_test.test)
            nursery.start_soon(trio_test.test)
            nursery.start_soon(trio_test.test)