#!/usr/bin/env python
# -*- coding:utf-8 -*-

import os.path

import tornado.httpserver
import tornado.ioloop
import tornado.web
import tornado.httpclient
from tornado.options import define, options

import settings as app_settings
from handlers import *

define("port", default=8080, help="port d'écoute du serveur http", type=int)
define("debug", default=False, help="activer le mode de débuggage", type=bool)
define("self_url", default="http://localhost:8080", help="URL du service", type=str)
where_am_i = os.path.dirname(__file__)

class Application(tornado.web.Application):
    def __init__(self, debug, self_url):
        handlers = [
            (r"/", HomeHandler)
            ]
        settings = {
            "titre": u"MeublesUTC !",
            'cookie_secret': app_settings.cookie_secret,
            "template_path": os.path.join(where_am_i, "templates"),
            "debug": debug,
            "sel_url": self_url
            }
        tornado.web.Application.__init__(self, handlers, **settings)

if __name__ == "__main__":
    tornado.options.parse_command_line()
    http_server = tornado.httpserver.HTTPServer(Application(options.debug, options.self_url))
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()
