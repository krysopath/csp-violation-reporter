#!/bin/python3
from aiohttp import web
import aiofiles
from datetime import datetime
from os import environ

import logging

logging.basicConfig(level=logging.DEBUG)
LOG_PATH = environ.get("CSP_LOG_FILE", "violations.log")

MSG = """timestamp: {} source: {} path_qs: {} payload: {}\n"""


async def handle(request):
    payload = await request.content.read()
    async with aiofiles.open(LOG_PATH, "a") as f:
        await f.write(
                MSG.format(
                    datetime.utcnow().timestamp(), 
                    request.remote, 
                    request.path_qs,
                    payload.decode(),
                )
        )
    return web.json_response({"result": True})

app = web.Application()
app.add_routes([
    web.post('/', handle),
])

if __name__ == '__main__':
    web.run_app(app, port=6000)

