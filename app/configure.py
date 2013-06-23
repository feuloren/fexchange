#!/usr/bin/env python
# -*- coding:utf-8 -*-

from os import urandom
from hashlib import md5
import os.path
from re import search

modele = """#!/usr/bin/env python
# -*- coding:utf-8 -*-

from .configure import locate

settings_model_hash = "{hash}"
def up_to_date():
    from hashlib import md5
    content = open(locate('settings_dist.py'), 'r').read()
    return settings_model_hash == md5(content).hexdigest()

"""

where_am_i = os.path.abspath(os.path.dirname(__file__))
def locate(name):
    return os.path.join(where_am_i, name)

def calculate_hash():
    return md5(open(locate('settings_dist.py'), 'r').read()).hexdigest()

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
    if os.path.isfile(locate('settings.py')):
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

    with open(locate('settings.py'), 'w') as settings:
        # On sauvegarde le hash md5 du fichier de config des paramètres
        # puis les paramètres
        settings.write(modele.format(hash=calculate_hash()))
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
    
    content = open(locate('settings.py'), 'r').read()
    old_hash = search(r'settings_model_hash = "(.+)"', content).group(1)
    content = content.replace(old_hash, calculate_hash())
    with open(locate('settings.py'), 'w') as settings_f:
        settings_f.write(content)
        settings_f.write(params)
