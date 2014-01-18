# -*- coding:utf-8 -*-

import tornado.web
from .base import BaseHandler
from ..models import *
from .. import forms

from sqlalchemy import and_

class ShowOffreHandler(BaseHandler):
    titre_ = 'Offre'

    def get_categories(self):
        return [(c.id, c.nom) for c in self.db.query(Categorie).all()]

    def get(self, id):
        offre = self.db.query(Offre).get(int(id))
        if offre is None:
            self.render("obj_not_found.html")
        else:
            self.titre = offre.nom
            if self.current_user:
                if self.current_user is offre.vendeur:
                    self.render("offre_manage.html", offre=offre)
                else:
                    # On récupère les messages échangés pour l'offre actuelle
                    # Entre le vendeur et l'utilisateur connecté
                    users = [self.current_user.id, offre.vendeur.id]
                    messages = self.db.query(Message).filter(and_(Message.offre_id == offre.id, Message.destinataire_id.in_(users), Message.emetteur_id.in_(users)))
                    self.render("offre_show.html", offre=offre, messages=messages)
            else:
                self.render("offre_show.html", offre=offre, messages=[])
