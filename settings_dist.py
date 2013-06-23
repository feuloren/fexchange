#!/usr/bin/env python
# -*- coding:utf-8 -*-

from os import urandom
from hashlib import sha256

# Liste des paramètres de l'application :
# Il peuvent être autogénéres (ex: cookie_secret)
# ou demandés à l'utilisateur
liste = [
    dict(name='cookie_secret', gen=(lambda : sha256(urandom(24)).hexdigest())),
    dict(name='db_user', desc="Nom de l'utilisateur pour la base de données", 
     default="root"),
    dict(name='db_pass', desc="Mot de passe pour la base de données", 
     default="root"),
    dict(name='db_host', desc="Emplacement du serveur de bases de données", 
     default="localhost"),
    dict(name='db_name', desc="Nom de la base de données", 
     default="fexchange"),
    dict(name='static_url', desc="Url d'accès aux fichiers statiques",
     default="/static/"),
    dict(name='cas_url', desc="Url du CAS", default="http://localhost/cas"),
    dict(name='service_url', desc="URL d'accès à l'application"),
    dict(name='port', desc="Port sur lequel écouter les requêtes",
         default="8080"),
]

