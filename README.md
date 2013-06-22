Revente de meubles entre UTCéens
================================

Pour revendre, donner, prêter et trouver des meubles à Compiègne.

Dépendances
-----------

Python2, Tornado, SqlAlchemy, Mysql, WTForms et pyScss

Installation
------------

Vous pouvez utilisez le script bootstrap_fexchange.py pour créer un virtualenv et installer les librairies python nécessaires.
Sous ubuntu il faut au préalable installer python-virtualenv et libmysqlclient-dev

Pour activer le virtualenv
```
source virtualenv/bin/activate
```

Pour en sortir
```
deactivate
```

Lancement
---------

```
./fexchange
```

Il est possible de configurer le serveur grâce à l'option --do
Voici les actions disponibles pour le moment
 * configure : Crée le fichier de configuration settings.py
 * create_tables : crée les tables à partir des modèles
 * drop_tables : supprime les tables de la base
