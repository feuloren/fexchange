# -*- coding:utf-8 -*-

from models import *
from wtforms.fields import PasswordField
from .base import BaseForm
from hashlib import sha512

def hash_user_password(mdp):
    if mdp:
        return sha512(mdp).hexdigest()

class CasForm(BaseForm):
    class Meta:
        model = Utilisateur

    mdp = PasswordField(u'Mot de Passe',
                        filters = [hash_user_password,])

    def customize(self):
        self.set_label('nom', u'Nom')
        self.set_label('prenom', u'Prénom')
        self.set_label('email', u'Adresse mail')

class UtilisateurForm(CasForm):
    class Meta:
        model = Utilisateur
        exclude = ['login']
