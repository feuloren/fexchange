# -*- coding:utf-8 -*-

from hashlib import sha512
from .base import BaseHandler
from models import Utilisateur
from forms import UtilisateurForm, MultiDict

class PasswordAuthHandler(BaseHandler):
    def get(self):
        self.render('password_auth.html', error=None)

    def post(self):
        email = self.get_argument('email', None)
        password = self.get_argument('password', None)
        password_hash = sha512(password).hexdigest()
        if not(email) or not(password):
            self.render('password_auth.html', error='Merci de compléter les champs')
        else:
            user = self.db.query(Utilisateur).filter_by(email=email, mdp=password_hash).first()
            if user:
                self.set_secure_cookie('user', str(user.id))
                self.set_secure_cookie('auth', 'classic')
                self.redirect("/")
            else:
                self.render('password_auth.html', error='Email ou mot de passe incorrect')

class RegisterHandler(BaseHandler):
    def get(self):
        form = UtilisateurForm()
        self.render('register.html', form=form)

    def post(self):
        form = UtilisateurForm()
        form.process(MultiDict(self))
        if form.validate():
            user = Utilisateur()
            form.populate_obj(user)
            self.db.add(user)
            self.db.commit()

            self.set_secure_cookie('user', str(user.id))
            self.set_secure_cookie('auth', 'classic')
            self.redirect('/')
        else:
            self.render('register.html', form=form)
