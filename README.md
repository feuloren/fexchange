Revente de meubles entre UTCéens
================================

Pour revendre, donner, prêter et trouver des meubles à Compiègne.

Dépendances
-----------

Python2, Tornado, SqlAlchemy et Alembic, Mysql, WTForms, pyScss

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

Il peut être utile de mettre à jour le virtualenv après avoir fait un pull
```
python update_virtualenv.py
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
 * migrate_db : Exécute toutes les migrations non-effectuées

L'option -d ou --debug passe l'application en mode debug :
 * Le serveur est relancé si un fichier python est modifié
 * Les fichiers scss sont recompilés quand ils sont modifiés

Migrations
----------

Les migrations de la base de données sont gérées grâce à Alembic,

Pour migrer la base vers la dernière vesion
```
alembic upgrade head
```

Pour créer une migration le mode automatique suffit généralement
```
alembic revision --autogenerate -m 'Nom de la révision'
```
Cette commande compare la base de données actuelle avec les modèles définis dans app/models.py
Elle crée un fichier de migration dans migrations/versions, il convient de vérifier ce fichier après qu'il ait été généré.
Finalement il suffit de faire la migration, puis ajouter le fichier de migration à git pour que les autres développeurs ou utilisateurs puissent migrer leur base.