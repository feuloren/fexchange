#!/usr/bin/env python
# -*- coding:utf-8 -*-

import sys
import optparse
from configure import interactive_config

parser = optparse.OptionParser()
parser.add_option('-p', '--port', dest='port', type='int', default=8080, action='store', help=u'Port sur lequel on écoute les connections')
parser.add_option('-u', '--url', dest='url', default='http://localhost:8080', action='store', help=u'URL d\'accès à l\'application')
parser.add_option('-d', '--debug', dest='debug', default=False, action='store_true', help=u'Lancement en mode debug')
parser.add_option('-D', '--do', dest='action', nargs=1, action='store', default=False, help=u'Action à effectuer (pour le déploiement et la maintenance)')

options, args = parser.parse_args()

if options.action:
    action = options.action
    if action == 'create_tables':
        import models
        print "= Création des tables ="
        models.metadata.create_all(models.engine)
        print "= Succès "

    elif action == 'drop_tables':
        import models
        print "= Suppression des tables ="
        models.metadata.drop_all(models.engine)
        print "= Succès ="

    elif action == 'configure':
        print "= Configuration interactive ="
        interactive_config()

    else:
        print "Action invalide"
    
else:
    import server
    print "= Lancement du serveur ="
    server.run(options.debug, options.url, options.port)
