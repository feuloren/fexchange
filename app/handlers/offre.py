# -*- coding:utf-8 -*-

import tornado.web
from .base import BaseHandler
from ..models import *
from .. import forms

class ShowOffreHandler(BaseHandler):
    titre_ = 'Vente'

    def get_categories(self):
        return [(c.id, c.nom) for c in self.db.query(Categorie).all()]

    def get(self, id):
        vente = self.db.query(Offre).get(int(id))
        if vente is None:
            self.render("obj_not_found.html")
        else:
            if self.current_user:
                if self.current_user is vente.vendeur:
                    self.render("vente_manage.html", vente=vente)
                else:
                    # messages = vente.message.filter((de = self.user and pour = vente.vendeur) or (de = vente.vendeur and to=self.user)).order_by(date_envoi)
                    self.rendeur("vente_show.html", vente=vente, messages=vente.message)
            else:
                self.render("vente_show.html", vente=vente)
