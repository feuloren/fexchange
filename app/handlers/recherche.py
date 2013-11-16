# -*- coding:utf-8 -*-

from .base import BaseHandler
from ..models import Offre, Utilisateur

class RechercheHandler(BaseHandler):
    titre_ = 'Rechercher un meuble'
    def get(self):
        term = self.get_argument('q', None)
        ventes = self.get_argument('accept-ventes', True)
        dons = self.get_argument('accept-dons', True)
        prets = self.get_argument('accept-prets', True)
        if term is None:
            results = None
        else:
            results = self.db.query(Offre).filter(Offre.nom.like('%'+term+'%')).limit(20)
        self.render("recherche.html", term = term,
                    results = results)
