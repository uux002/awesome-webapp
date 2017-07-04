import logging

import asyncio, os, json, time
from datetime import datetime
from aiohttp import web

logging.basicConfig(level=logging.INFO)

async def read_server_ip_port():
    with open('ip_config','r') as f:
        ip = f.readline()
        port = f.readline()
        return ip.strip(),port.strip()

async def index(request):
    return web.Response(body=b'<h1>Awesome App</h1>', content_type='text/html')

async def init(loop):
    ip,port = await read_server_ip_port()
    app = web.Application(loop = loop)
    app.router.add_route('GET','/',index)
    #srv = await loop.create_server(app.make_handler(),'127.0.0.1',9000)
    srv = await loop.create_server(app.make_handler(), ip, port)
    logging.info('server started at %s:%s ...' % (ip,port))
    return srv


loop = asyncio.get_event_loop()
loop.run_until_complete(init(loop))
loop.run_forever()


