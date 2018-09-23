import logging

import aiohttp_jinja2
import jinja2
from aiohttp import web

from db import init_pg, close_pg
from middlewares import setup_middlewares
from routes import setup_routes
from settings import get_config


async def init_app():
    app = web.Application()

    app['config'] = get_config()

    # setup Jinja2 template renderer
    aiohttp_jinja2.setup(app, loader=jinja2.PackageLoader('templates'))

    # create db connection on startup, shutdown on exit
    app.on_startup.append(init_pg)
    app.on_cleanup.append(close_pg)

    # setup routes and middlewares
    setup_routes(app)
    setup_middlewares(app)

    return app


def main():
    logging.basicConfig(level=logging.DEBUG)
    app = init_app()
    web.run_app(app)


if __name__ == '__main__':
    main()
