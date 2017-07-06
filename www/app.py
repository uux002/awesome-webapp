# _*_ coding: utf-8 _*_

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
    #text = '<h1>Awesome App <br> %s </h1>' % time.strftime("%Y-%m-%d %H:%M:%S",time.localtime())
    text = '<h5>永远不要让其他人知道你是谁!<h5>'
    return web.Response(body=text.encode('gb2312'), content_type='text/html')

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


