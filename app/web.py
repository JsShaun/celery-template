import asyncio
import tornado.web
from process import http



class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello, world")

    def post(self):
        result = http.delay()

        rsp = {}
        rsp['result'] = result.id
        rsp['state'] = result.state

        self.write(rsp)

def make_app():
    return tornado.web.Application([
        (r"/", MainHandler),
    ])

async def main():
    app = make_app()
    app.listen(8888)
    await asyncio.Event().wait()

if __name__ == "__main__":
    asyncio.run(main())