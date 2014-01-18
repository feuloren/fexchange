#!/usr/bin/env python
# -*- coding: utf-8 -*-

import logging
logging.basicConfig(format="%(levelname)s  [%(name)s] %(message)s")
logger = logging.getLogger('test_server')
logger.setLevel(logging.INFO)

def update_settings():
    import app.settings as app_settings
    app_settings.port = '8888'
    app_settings.db_name = 'fexchange_test'
    app_settings.static_url = "http://localhost:8888/static/"
    app_settings.service_url = "http://localhost:8888"

def fill_db():
    from alembic.config import Config
    from alembic import command
    
    alembic_cfg = Config("alembic.ini")
    command.upgrade(alembic_cfg, "head")

def clean_db():
    from alembic.config import Config
    from alembic import command
    
    alembic_cfg = Config("alembic.ini")
    command.downgrade(alembic_cfg, "base")

def run():
    """Effectue les migrations sql depuis le début,
    et lance le serveur
    """
    update_settings()
    logger.info("Settings updated")

    logger.info("Starting migrations")
    fill_db()
    logger.info("Migrations done")

    from app.server import run as run_server
    try:
        logger.info("Starting server")
        run_server()
    except KeyboardInterrupt:
        logger.info("Server interrupted")
        #logger.info("Starting to clean the DB")
        #clean_db()
        #logger.info("Cleaning done, exiting")

if __name__ == '__main__':
    run()
