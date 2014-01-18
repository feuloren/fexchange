#-*- coding: utf-8 -*-

import tornado.web
from .base import BaseHandler

class LoginHandler(BaseHandler):
    titre_ = "Connexion"

    def get(self):
        # on récupère l'url qui a demandé l'authentification
        # TODO : regarder le aussi referer si on a pas de next

        url = self.get_argument('next', '/')
        self.set_cookie('auth_target_url', url)
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
