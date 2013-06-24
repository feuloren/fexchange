# -*- coding:utf-8 -*-

from .base import BaseHandler
from ..models import Offre, Utilisateur

class RechercheHandler(BaseHandler):
    def get(self, term):
        if term is None:
            results = None
        else:
            results = self.db.query(Offre).filter(Offre.nom.like('%'+term+'%')).limit(20)
        self.render("recherche.html", term = term,
                    results = results)
