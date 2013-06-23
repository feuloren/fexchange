#!/usr/bin/env python
# -*- coding:utf-8 -*-

import sys
import os
import optparse
from app.configure import interactive_config, update

parser = optparse.OptionParser()
parser.add_option('-d', '--debug', dest='debug', default=False, action='store_true', help=u'Lancement en mode debug')
parser.add_option('-D', '--do', dest='action', nargs=1, action='store', default=False, help=u'Action à effectuer (pour le déploiement et la maintenance)')

options, args = parser.parse_args()

assets_conf_compile = dict(
    source = 'assets/styles',
    target = 'static/styles',
    compress = False)
assets_conf_watch = dict(
    source = 'assets/styles',
    target = 'static/styles',
    compress = False)

try:
    os.environ['VIRTUAL_ENV']
except KeyError:
    print """############
## Attention
## Vous n'êtes pas dans le virtualenv,
## référez vous au fichier README.md pour plus d'informations
############"""

try:
    import app.settings
except ImportError:
    print "- Configuration de l'application -"
    interactive_config()
    import app.settings

if not app.settings.up_to_date():
    print "- Mise à jour du fichier de paramètres -"
    update()
    reload(app.settings)

if options.action:
    action = options.action
    if action == 'create_tables':
        from app import models
        print "= Création des tables ="
        models.metadata.create_all(models.engine)
        print "= Succès "

    elif action == 'drop_tables':
        from app import models
        print "= Suppression des tables ="
        models.metadata.drop_all(models.engine)
        print "= Succès ="

    elif action == 'configure':
        print "= Configuration interactive ="
        interactive_config()

    elif action == 'compile_assets':
        print "= Compilation des ressources ="
        from app.assets_manager import compile
        compile(**assets_conf_compile)

    else:
        print "Action invalide"
    
else:
    from app import server
    print "= Lancement du serveur ="
    if options.debug:
        print "- Mode Débug -"
        from app.assets_manager import watch
        watch(**assets_conf_watch)
    server.run(options.debug)
