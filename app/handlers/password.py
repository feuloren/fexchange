# -*- coding:utf-8 -*-

from passlib.hash import pbkdf2_sha256

# cf http://en.wikipedia.org/wiki/PBKDF2
# pbkdf2 est un algorithme qui permet d'obtenir une clé à partir d'un mot de passe
# cf http://pythonhosted.org/passlib/lib/passlib.hash.pbkdf2_digest.html

salt_length = 20
pbkdf2_rounds = 10000

def verify(hash, input):
    "Compare la valeur de clé stockée avec le mot de passe envoyée par l'utilisateur"
    return pbkdf2_sha256.verify(input, hash)

def encrypt(password):
    "Crée un hash sécurisé à partir d'un mot de passe"
    return pbkdf2_sha256.encrypt(password)
