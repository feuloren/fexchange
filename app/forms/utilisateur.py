# -*- coding:utf-8 -*-

from ..models import *
from wtforms.fields import PasswordField
from .base import BaseForm
from ..handlers.password import encrypt

class CasForm(BaseForm):
    class Meta:
        model = Utilisateur

    mdp = PasswordField(u'Mot de Passe',
                        filters = [lambda p : None if p is None else encrypt(p),])

    def customize(self):
        self.set_label('nom', u'Nom')
        self.set_label('prenom', u'Prénom')
        self.set_label('email', u'Adresse mail')

class UtilisateurForm(CasForm):
    class Meta:
        model = Utilisateur
        exclude = ['login']
