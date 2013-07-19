# -*- coding:utf-8 -*-

import tornado.web
from .base import BaseHandler
from ..models import *
from .. import forms
from datetime import datetime

class NewVenteHandler(BaseHandler):
    titre_ = 'Vendre un meuble'

    def get_categories(self):
        return [(c.id, c.nom) for c in self.db.query(Categorie).all()]

    @tornado.web.authenticated
    def get(self):
        form = forms.VenteForm()
        form.categorie_id.choices = self.get_categories()
        self.render("new_vente.html", form = form)

    @tornado.web.authenticated
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

class NewPretHandler(BaseHandler):
    titre_ = u'Prêter un meuble'

    def get_categories(self):
        return [(c.id, c.nom) for c in self.db.query(Categorie).all()]

    @tornado.web.authenticated
    def get(self):
        form = forms.PretForm()
        form.categorie_id.choices = self.get_categories()
        self.render("new_pret.html", form = form)

    @tornado.web.authenticated
    def post(self):
        auto_values = dict(vendeur_id=1,
                           type='pret',
                           date_depart=datetime.now(),
                           )
        form = forms.PretForm()
        form.categorie_id.choices = self.get_categories()
        form.process(forms.MultiDict(self), **auto_values)
        if form.validate():
            pret = Pret()
            form.populate_obj(pret)
            self.db.add(pret)
            self.db.commit()
            self.redirect('/')
        else:
            self.render("new_pret.html", form = form)

class NewDonHandler(BaseHandler):
    titre_ = 'Vendre un meuble'

    def get_categories(self):
        return [(c.id, c.nom) for c in self.db.query(Categorie).all()]

    @tornado.web.authenticated
    def get(self):
        form = forms.DonForm()
        form.categorie_id.choices = self.get_categories()
        self.render("new_don.html", form = form)

    @tornado.web.authenticated
    def post(self):
        auto_values = dict(vendeur_id=1,
                           type='don',
                           date_depart=datetime.now(),
                           )
        form = forms.DonForm()
        form.categorie_id.choices = self.get_categories()
        form.process(forms.MultiDict(self), **auto_values)
        if form.validate():
            don = Don()
            form.populate_obj(don)
            self.db.add(don)
            self.db.commit()
            self.redirect('/')
        else:
            self.render("new_don.html", form = form)
