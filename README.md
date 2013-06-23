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

Pour créer le virtualenv
```
python bootstrap_fexchange.py
```

Pour activer le virtualenv
```
source activate
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
 * create_tables : Crée les tables à partir des modèles
 * drop_tables : Supprime les tables de la base
 * compile_assets : Compile les fichiers scss

L'option -d ou --debug passe l'application en mode debug :
 * Le serveur est relancé si un fichier python est modifié
 * Les fichiers scss sont recompilés quand ils sont modifiés
