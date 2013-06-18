#!/usr/bin/env python
# -*- coding:utf-8 -*-

from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String, DateTime, Boolean, Text, ForeignKey, Enum
from sqlalchemy.orm import relationship, backref, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

import settings as app_settings

engine = create_engine(app_settings.db_connection, echo=False)
#Session = sessionmaker(bind=engine)
#session = Session()
Base = declarative_base()

class Utilisateur(Base):
    __tablename__ = 'utilisateurs'
    id = Column(Integer, primary_key=True)
    login = Column(String(10), nullable=False)
    prenom = Column(String(30), nullable=False)
    nom = Column(String(30), nullable=False)
    email = Column(String(100), nullable=False)
    mdp = Column(String(128), nullable=False)
    offres = relationship("Offre", order_by="Offre.id", backref="offre")

    def __repr__(self):
        return "<User('%s')>" % (self.login)

utilisateurs_table = Utilisateur.__table__

class Offre(Base):
    __tablename__ = 'offres'
    id = Column(Integer, primary_key=True)
    vendeur_id = Column(Integer, ForeignKey('utilisateurs.id'), nullable=False)
    vendeur = relationship("Utilisateur")
    type = Column(Enum('pret', 'don', 'vente', 'achat'), nullable=False)
    nom = Column(String(20), nullable=False)
    categorie_id = Column(Integer, ForeignKey('categories.id'), nullable=False)
    categorie = relationship("Categorie")
    description = Column(Text)
    date_depart = Column(DateTime, nullable=False)
    date_conclusion = Column(DateTime)
    date_annule = Column(DateTime)

offres_table = Offre.__table__

class Categorie(Base):
    __tablename__ = 'categories'
    id = Column(Integer, primary_key=True)
    nom = Column(String(20), nullable=True)
    description = Column(String(140), nullable=True)

categories_table = Categorie.__table__

class Photo(Base):
    __tablename__ = 'photos'
    id = Column(Integer, primary_key=True)
    offre_id = Column(Integer, ForeignKey('offres.id'), nullable=True)
    offre = relationship("Offre", backref=backref('photos', order_by=id))
    description = Column(Text)
    date_upload = Column(DateTime, nullable=True)

photos_table = Photo.__table__

metadata = Base.metadata

def create_all():
    metadata.create_all(engine)
