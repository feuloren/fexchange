# -*- coding:utf-8 -*-

from ..handlers.password import *

def test_ok():
    from os import urandom
    from random import randrange

    # On génère un mot de passe aléatoire
    pass_length = randrange(4, 10)
    password = urandom(pass_length)

    # On le chiffre
    encrypted = encrypt(password)

    # Et on vérifie qu'on peut bien le déchiffrer
    assert verify(encrypted, password)
    # Et qu'une chaine aléatoire ne le dévérouille pas
    assert not(verify(encrypted, urandom(pass_length)))
