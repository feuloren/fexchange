# -*- coding:utf-8 -*-

import tornado.web
from .base import BaseHandler
from ..models import *
from .. import forms

class ShowOffreHandler(BaseHandler):
    titre_ = 'Offre'

    def get_categories(self):
        return [(c.id, c.nom) for c in self.db.query(Categorie).all()]

    def get(self, id):
        offre = self.db.query(Offre).get(int(id))
        if offre is None:
            self.render("obj_not_found.html")
        else:
            if self.current_user:
                if self.current_user is offre.vendeur:
                    self.render("offre_manage.html", offre=offre)
                else:
                    # messages = offre.message.filter((de = self.user and pour = offre.vendeur) or (de = offre.vendeur and to=self.user)).order_by(date_envoi)
                    self.render("offre_show.html", offre=offre, messages=offre.messages)
            else:
                self.render("offre_show.html", offre=offre)
