#!/usr/bin/env python
# -*- coding:utf-8 -*-

from os import urandom
from hashlib import sha256, md5
import os.path

modele = """
#!/usr/bin/env python
# -*- coding:utf-8 -*-

settings_model_hash = "{hash}"
def up_to_date():
    from hashlib import md5
    content = open('settings_dist.py', 'r').read()
    return settings_model_hash == md5(content).hexdigest()

"""

def ask(message, default=None):
    """Demande une valeur à l'utilisateur
    Il est possible de donner une valeur par défaut qui sera
    indiquée à l'utilisateur et renvoyée si il entre une chaine vide
    """
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

def yes_or_no(message):
    res = 'a'
    while not(res in ('o', 'n')):
        res = raw_input(message + ' [o/n] : ')
    return res == 'o'

def get_value(param):
    if param.has_key('gen'):
        return param['gen']()
    else:
        if not param.has_key('desc'):
            raise Exception("Le paramètre %s n'a pas de description !" % param['name'])
        default = param.get('default', None)
        return ask(param['desc'], default)

def interactive_config():
    if (os.path.isfile('settings.py')):
        import settings
        if not settings.up_to_date():
            if yes_or_no('Le fichier de paramètre à été modifié, mettre à jour ?'):
                return update()
        if not yes_or_no('Le fichier de configuration existe déjà, écraser cette configuration ?'):
            print "Abandon"
            return

    params = ''
    import settings_dist
    for param in settings_dist.liste:
        if not param.has_key('name'):
            raise Exception("Le paramètre " + str(param) + " n'a pas de nom !")
        value = get_value(param)
        params += '{name} = "{value}"\n'.format(name=param['name'],
                                              value=value)

    with open('settings.py', 'w') as settings:
        # On sauvegarde le hash md5 du fichier de config des paramètres
        # puis les paramètres
        hash = md5(open('settings_dist.py', 'r').read()).hexdigest()
        settings.write(modele.format(hash=hash))
        settings.write(params)


def update():
    params = ''
    import settings_dist
    import settings
    for param in settings_dist.liste:
        if not param.has_key('name'):
            raise Exception("Le paramètre " + str(param) + " n'a pas de nom !")
        if hasattr(settings, param['name']):
            continue
        value = get_value(param)
        params += '{name} = "{value}"\n'.format(name=param['name'],
                                                value=value)

    with open('settings.py', 'a') as settings_f:
        settings_f.write(params)
