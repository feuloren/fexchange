# -*- coding:utf-8 -*-

import logging
from logging.handlers import TimedRotatingFileHandler
import inspect

def initial_config():
    # On crée un logger principal 'app' et on le configure
    # Dès qu'un module récupérera un module il sera considéré
    # comme fils du logger principal et héritera de sa config
    # Genre 'app.server', 'app.handlers.home'...
    logger = logging.getLogger(__name__.split('.')[0])
    logger.setLevel(logging.INFO)
    handler = TimedRotatingFileHandler('logs/log', 'midnight')
    handler.setFormatter(logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s'))
    logger.addHandler(handler)
    return logger

# Le code n'est exécuté que lors du premier import
main_logger = initial_config()

def logger_factory(name=None):
    # Si aucun nom n'est précisé on le récupère depuis
    # la pile d'appels de la fonction
    if name is None:
        frame = inspect.stack()[1]
        name = inspect.getmodule(frame[0]).__name__

    return logging.getLogger(name)
