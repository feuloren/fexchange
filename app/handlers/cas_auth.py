# -*- coding:utf-8 -*-

import re
import tornado.web
from .base import BaseHandler
from ..models import Utilisateur
from ..forms import CasForm, MultiDict
from .password import encrypt
from random import choice
import string

# Password generation
chars = string.letters + string.digits
length = 8

class CasHandler(BaseHandler):
    @tornado.web.asynchronous
    def get(self):
        ticket = self.get_argument("ticket", None)
        if ticket:
            # On a un ticket, on va le valider 
            def callback(reponse):
                data = re.search("<cas:user>([a-z]{1,8})</cas:user>", reponse.body)
                if data:
                    login = data.group(1)
                    user = self.db.query(Utilisateur).filter_by(login=login).first()
                    if user:
                        self.set_logged_user(user, 'cas')
                    else:
                        self.set_secure_cookie('register_cas_user', login)
                        self.redirect("/auth/cas/register")
                else:
                    self.write("Erreur d'authentification, merci de contacter le webmaster")
                    self.finish()

            try:
                http = tornado.httpclient.AsyncHTTPClient()
                reponse = http.fetch(self.cas_validate(ticket), callback)
            except tornado.httpclient.HTTPError as he:
                self.redirect(self.cas_login())
        else:
            self.redirect(self.cas_login())

class CasRegisterHandler(BaseHandler):
    def get(self):
        form = CasForm()
        self.render('cas_register.html', form=form)

    def post(self):
        login = self.get_secure_cookie('register_cas_user')
        if not login:
            self.redirect('/')

        form = CasForm()
        form.process(MultiDict(self))
        if form.validate():
            user = Utilisateur()
            form.populate_obj(user)
            user.login = login
            user.mdp = encrypt(''.join(choice(chars) for _ in range(length)))
            self.db.add(user)
            self.db.commit()

            self.set_secure_cookie('user', str(user.id))
            self.set_secure_cookie('auth', 'cas')
            self.clear_cookie('register_cas_user')
            self.redirect('/')
        else:
            self.render('cas_register.html', form=form)
