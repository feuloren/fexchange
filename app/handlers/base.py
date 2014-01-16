# -*- coding:utf-8 -*-

import tornado.web
from ..models import Utilisateur

class BaseHandler(tornado.web.RequestHandler):
    def __init__(self, application, request, **kwargs):
        super(BaseHandler, self).__init__(application, request, **kwargs)

        self.db = self.application.db()

    def get_current_user(self):
        user_id = self.get_secure_cookie("user")
        if not user_id:
            self.current_user = None
        else:
            self.current_user = self.db.query(Utilisateur).get(int(user_id))
        return self.current_user

    def static_url(self, filename):
        """On stocke nos fichiers statiques sous un autre domaine.
        et on n'a pas besoin du versionnage des fichiers"""
        self.require_setting("static_url")
        
        return self.application.settings["static_url"] + filename

    @property
    def titre(self):
        self.require_setting("titre")

        if hasattr(self, 'titre_'):
            return '%s - %s' % (self.titre_, self.settings['titre'])
        else:
            return self.settings['titre']

    @titre.setter
    def titre(self, val):
        self.titre_ = val

    @property
    def service_url(self):
        self.require_setting('service_url')
        return self.settings['service_url']

    @property
    def cas_url(self):
        self.require_setting('cas_url')
        return self.settings['cas_url']

    def set_logged_user(self, user, method):
        self.set_secure_cookie('user', str(user.id))
        self.set_secure_cookie('auth', method)
        url = self.get_cookie('auth_target_url', '/')
        self.redirect(url)

    # Generate CAS URLs
    def cas_login(self):
        return self.cas_url + "/login?service=" + self.service_url + self.reverse_url('cas_auth')

    def cas_validate(self, ticket):
        return self.cas_url + "/serviceValidate?service=" + self.service_url + self.reverse_url('cas_auth') + "&ticket=" + ticket

    def cas_logout(self):
        return self.cas_url + "/logout?url=" + self.service_url

