#!/usr/bin/env python
# -*- coding:utf-8 -*-

#Secret key for tornado secure cookies
cookie_secret = "{secret}"
#Database connection string
db_connection = "{type}://{user}:{password}@{location}/{base}"
#Emplacement des fichiers statiques, utilisé pour servir les fichiers en mode debug, et pour les déployer sinon
static_path = "{static_path}"
#URL par laquelle on peut accéder aux fichiers statiques en production
static_host = "{static_host}"
