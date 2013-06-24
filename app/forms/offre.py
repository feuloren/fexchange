# -*- coding:utf-8 -*-

from ..models import *
from .base import BaseForm
from wtforms.fields import IntegerField, SelectField

class OffreForm(BaseForm):
    class Meta:
        model = Offre

class VenteForm(BaseForm):
    class Meta:
        model = Vente
        include_foreign_keys = True

    vendeur_id = IntegerField()
    categorie_id = SelectField(u'Catégorie', coerce=int)

    def customize(self):
        self.set_label("nom", u"Nom de l'objet")
        self.set_label("date_disponibilite", u"Date de disponibilité de l'objet")
        self.set_label("date_achat", u"Date d'achat")
        self.set_label("prix", u"Prix")
        self.set_label("etat", u"État")

