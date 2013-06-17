#!/usr/bin/env python
# -*- coding:utf-8 -*-

import os.path

import tornado.httpserver
import tornado.ioloop
import tornado.web
import tornado.httpclient
from tornado.options import define, options

from sqlalchemy.orm import scoped_session, sessionmaker
from models import *  # import the engine to bind

import settings as app_settings
from handlers import *

where_am_i = os.path.dirname(__file__)

class Application(tornado.web.Application):
    def __init__(self, debug, self_url):
        handlers = [
            (r"/", HomeHandler)
            ]
        settings = {
            "titre": u"Adopte un meuble",
            'cookie_secret': app_settings.cookie_secret,
            "template_path": os.path.join(where_am_i, "templates"),
            "debug": debug,
            "self_url": self_url
            }
        tornado.web.Application.__init__(self, handlers, **settings)
        # Have one global connection.
        self.db = scoped_session(sessionmaker(bind=engine))

def run(debug=False, self_url='localhost:8080', port=8080):
    http_server = tornado.httpserver.HTTPServer(Application(debug, self_url))
    http_server.listen(port)
    tornado.ioloop.IOLoop.instance().start()

if __name__ == "__main__":
    run()
