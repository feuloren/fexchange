# -*- coding:utf-8 -*-

from wtforms_alchemy import model_form_factory
from wtforms.ext.i18n.form import Form as I18NForm

ModelForm = model_form_factory(I18NForm)
ModelForm.LANGUAGES = ['fr_FR', 'fr']

class FieldError(Exception):
    pass

class MultiDict(object):
    """Interface pour que WTF puisse accèder aux arguments de la requête
    (copié depuis le lazy web)
    """
    def __init__(self, handler):
        self.handler = handler

    def __iter__(self):
        return iter(self.handler.request.arguments)

    def __len__(self):
        return len(self.handler.request.arguments)

    def __contains__(self, name):
        # We use request.arguments because get_arguments always returns a
        # value regardless of the existence of the key.
        return (name in self.handler.request.arguments)

    def getlist(self, name):
        # get_arguments by default strips whitespace from the input data,
        # so we pass strip=False to stop that in case we need to validate
        # on whitespace.
        return self.handler.get_arguments(name, strip=False)

class BaseForm(ModelForm):
    """Formulaire de base pour fexchange,
    après l'initialisation la fonction customize() est appelée
    Il faut personnaliser les labels dans cette function grâce à set_label
    """
    def __init__(self, *args, **kwargs):
        super(BaseForm, self).__init__(*args, **kwargs)
        try:
            self.customize()
        except AttributeError:
            pass

    def set_label(self, name, label):
        try:
            self[name].label.text = label
        except KeyError:
            raise FieldError(name)

