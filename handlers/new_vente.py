# -*- coding:utf-8 -*-

from .base import BaseHandler
from models import Vente, Utilisateur, Categorie
import forms
from datetime import datetime

class NewVenteHandler(BaseHandler):
    def get_categories(self):
        return [(c.id, c.nom) for c in self.db.query(Categorie).all()]

    def get(self):
        form = forms.VenteForm()
        form.categorie_id.choices = self.get_categories()
        self.render("new_vente.html", form = form)

    def post(self):
        auto_values = dict(vendeur_id=1,
                           type='vente',
                           date_depart=datetime.now(),
                           )
        form = forms.VenteForm()
        form.categorie_id.choices = self.get_categories()
        form.process(forms.MultiDict(self), **auto_values)
        if form.validate():
            vente = Vente()
            form.populate_obj(vente)
            self.db.add(vente)
            self.db.commit()
            self.redirect('/')
        else:
            self.render("new_vente.html", form = form)
