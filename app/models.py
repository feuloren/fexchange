#!/usr/bin/env python
# -*- coding:utf-8 -*-

from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String, DateTime, Boolean, Text, ForeignKey, Enum, Numeric, Date
from sqlalchemy.orm import relationship, backref, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.ext.hybrid import hybrid_property
from sqlalchemy.engine.url import URL

import settings as app_settings

url = URL('mysql', username=app_settings.db_user,
          password=app_settings.db_pass,
          host=app_settings.db_host,
          database=app_settings.db_name,
          query={'charset':'utf8',
                 'use_unicode':'1'})
engine = create_engine(url, echo=False)
#Session = sessionmaker(bind=engine)
#session = Session()
Base = declarative_base()

class Utilisateur(Base):
    __tablename__ = 'utilisateurs'
    id = Column(Integer, primary_key=True)
    login = Column(String(10), nullable=True)
    prenom = Column(String(30), nullable=False)
    nom = Column(String(30), nullable=False)
    email = Column(String(100), nullable=False)
    mdp = Column(String(128), nullable=False) #sha512
    offres = relationship("Offre", order_by="Offre.id", backref="offre")

    @hybrid_property
    def nom_complet(self):
        return self.prenom + ' ' + self.nom

    def __repr__(self):
        return "<User('%s')>" % (self.login)

utilisateurs_table = Utilisateur.__table__

class Offre(Base):
    __tablename__ = 'offres'
    id = Column(Integer, primary_key=True)
    vendeur_id = Column(Integer, ForeignKey('utilisateurs.id'), nullable=False)
    vendeur = relationship("Utilisateur")
    type = Column(Enum('pret', 'don', 'vente'), nullable=False)
    nom = Column(String(20), nullable=False)
    categorie_id = Column(Integer, ForeignKey('categories.id'), nullable=False)
    categorie = relationship("Categorie")
    description = Column(Text)
    date_depart = Column(DateTime, nullable=False)
    date_conclusion = Column(DateTime)
    date_annule = Column(DateTime)

    date_achat = Column(Date)
    date_disponibilite = Column(Date, nullable=False)
    etat = Column(Enum(u'Neuf', u'Comme neuf', u'Bon état', u'Usé', u'Dégradé'), nullable=False)

    messages = relationship("Message", order_by="Message.date_envoi")

    __mapper_args__ = {
        'polymorphic_identity':'offres',
        'polymorphic_on':type
        }

class Don(Offre):
    __tablename__ = 'offres'

    __mapper_args__ = {
        'polymorphic_identity':'don',
        }

class Vente(Offre):
    __tablename__ = 'ventes'
    id = Column(Integer, ForeignKey('offres.id'), primary_key=True)
    prix = Column(Numeric(6, 2), nullable=True)

    __mapper_args__ = {
        'polymorphic_identity':'vente',
        }

class Pret(Offre):
    __tablename__ = 'prets'
    id = Column(Integer, ForeignKey('offres.id'), primary_key=True)
    date_retour = Column(Date)
    duree = Column(String(20))

    __mapper_args__ = {
        'polymorphic_identity':'pret',
        }

offres_table = Offre.__table__
dons_table = Don.__table__
ventes_table = Vente.__table__
prets_table = Pret.__table__

class Categorie(Base):
    __tablename__ = 'categories'
    id = Column(Integer, primary_key=True)
    nom = Column(String(20), nullable=False)
    description = Column(String(140))

categories_table = Categorie.__table__

class Photo(Base):
    __tablename__ = 'photos'
    id = Column(Integer, primary_key=True)
    offre_id = Column(Integer, ForeignKey('offres.id'), nullable=True)
    offre = relationship("Offre", backref=backref('photos', order_by=id))
    description = Column(Text)
    date_upload = Column(DateTime, nullable=True)

photos_table = Photo.__table__

class Message(Base):
    __tablename__ = 'messages'
    id = Column(Integer, primary_key=True)
    de = Column(Integer, ForeignKey('utilisateurs.id'), nullable=False)
    pour = Column(Integer, ForeignKey('utilisateurs.id'), nullable=False)
    offre = Column(Integer, ForeignKey('offres.id'))
    proposition = Column(Integer, ForeignKey('propositions.id'))
    contenu = Column(Text, nullable=False)
    date_envoi = Column(DateTime, nullable=False)
    date_lecture = Column(DateTime)

class Proposition(Base):
    __tablename__ = 'propositions'
    id = Column(Integer, primary_key=True)
    type = Column(Enum('pret', 'don', 'vente'), nullable=False)
    utilisateur = Column(Integer, ForeignKey('utilisateurs.id'), nullable=False)
    date_proposition = Column(DateTime, nullable=False)
    date_accepte = Column(DateTime)
    date_refuse = Column(DateTime)

    __mapper_args__ = {
        'polymorphic_identity':'propositions',
        'polymorphic_on':type
        }

class PropositionAchat(Proposition):
    __tablename__ = 'achats'
    id = Column(Integer, ForeignKey('propositions.id'), primary_key=True)
    prix = Column(Numeric(6, 2), nullable=True)

    __mapper_args__ = {
        'polymorphic_identity':'vente',
        }

class PropositionPret(Proposition):
    __tablename__ = 'pprets'
    id = Column(Integer, ForeignKey('propositions.id'), primary_key=True)
    date_retour = Column(Date)
    duree = Column(Integer)

    __mapper_args__ = {
        'polymorphic_identity':'pret',
        }

metadata = Base.metadata

def create_all():
    metadata.create_all(engine)
