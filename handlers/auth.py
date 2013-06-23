#-*- coding: utf-8 -*-

import tornado.web
from .base import BaseHandler
from .cas import CasHandler

class LoginHandler(BaseHandler):
    def get(self):
        self.render('auth.html')

class LogoutHandler(BaseHandler):
    @tornado.web.authenticated
    def get(self):
        method = self.get_secure_cookie('auth')
        self.clear_cookie('user')
        self.clear_cookie('auth')
        if method == 'cas':
            self.redirect(self.cas_logout())
        else:
            self.redirect('/')
