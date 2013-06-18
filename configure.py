#!/usr/bin/env python
# -*- coding:utf-8 -*-

from os import urandom
from hashlib import sha256
import os.path

modele = """#!/usr/bin/env python
# -*- coding:utf-8 -*-

cookie_secret = "{secret}"
db_connection = "{type}://{user}:{password}@{location}/{base}"

"""

def ask(message, default=None):
    res = raw_input(message + (' ['+default+']' if default else '') + ' : ')
    if res:
        return res
    else:
        if default:
            return default
        else:
            while not(res):
                res = raw_input(message + ' : ')
            return res

def interactive_config():
    if (os.path.isfile('settings.py')):
        res = 'a'
        while not(res in ('o', 'n')):
            res = raw_input('Le fichier de configuration existe déjà, écraser cette configuration ? [o/n] : ')
        if res == 'n':
            print "Abandon"
            return

    type = ask('Type de la base de données', 'mysql')
    user = ask('Nom de l\'utilisateur')
    password = ask('Mot de passe')
    location = ask('Emplacement du serveur', 'localhost')
    base = ask('Nom de la base de données')
    secret = sha256(urandom(24)).hexdigest()

    try:
        format = open('settings.dist.py', 'r').read()
    except Exception as e:
        format = modele

    with open('settings.py', 'w') as settings:
        settings.write(format.format(secret=secret,
                                     type=type,
                                     user=user,
                                     password=password,
                                     location=location,
                                     base=base))

