# -*- coding:utf-8 -*-

from .base import BaseHandler
from ..models import Offre, Utilisateur

class RechercheHandler(BaseHandler):
    titre_ = 'Rechercher un meuble'
    def get(self):
        term = self.get_argument('q', None)
        ventes = self.get_argument('ventes', False)
        dons = self.get_argument('dons', False)
        prets = self.get_argument('prets', False)
        if term is None:
            results = None
        else:
            q = self.db.query(Offre).filter(Offre.nom.like('%'+term+'%'))
            if not(ventes):
                q = q.filter(Offre.type != 'vente')
            if not(dons):
                q = q.filter(Offre.type != 'don')
            if not(prets):
                q = q.filter(Offre.type != 'pret')

            results = q.limit(20)
        self.render("recherche.html", term = term,
                    results = results)
