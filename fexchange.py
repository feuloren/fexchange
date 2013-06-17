#!/usr/bin/env python
# -*- coding:utf-8 -*-

import sys
import optparse

parser = optparse.OptionParser()
parser.add_option('-p', '--port', dest='port', type='int', default=8080, action='store')
parser.add_option('-u', '--url', dest='url', default='http://localhost:8080', action='store')
parser.add_option('-d', '--debug', dest='debug', default=False, action='store_true')
parser.add_option('-D', '--do', dest='action', nargs=1, action='store', default=False)

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

    else:
        print "Action invalide"
    
else:
    import server
    print "= Lancement du serveur ="
    server.run(options.debug, options.url, options.port)
