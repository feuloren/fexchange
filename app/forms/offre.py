# -*- coding:utf-8 -*-

from ..models import *
from .base import BaseForm
from wtforms.fields import IntegerField, SelectField

class OffreForm(BaseForm):
    vendeur_id = IntegerField()
    categorie_id = SelectField(u'Catégorie', coerce=int)

    def customize(self):
        self.set_label("nom", u"Nom de l'objet")
        self.set_label("description", u"Description")
        self.set_label("date_disponibilite", u"Date de disponibilité de l'objet")
        self.set_label("date_achat", u"Date d'achat")
        self.set_label("etat", u"État")

class VenteForm(OffreForm):
    class Meta:
        model = Vente
        include_foreign_keys = True

    def customize(self):
        super(VenteForm, self).customize()
        self.set_label("prix", u"Prix")

class PretForm(OffreForm):
    class Meta:
        model = Pret
        include_foreign_keys = True

    def customize(self):
        super(PretForm, self).customize()
        self.set_label("date_retour", u"Date de retour souhaitée")
        self.set_label("duree", u"Durée du prêt")

class DonForm(OffreForm):
    class Meta:
        model = Don
        include_foreign_keys = True
