# -*- coding:utf-8 -*-

from tornado.web import UIModule
import markdown

class FormField(UIModule):
    def render(self, field, **kwargs):
        # note : on peut vérifier si le champ est requis avec field.flags.required
        return self.render_string('modules/formfield.html', field=field, kwargs=kwargs)

class Markdown(UIModule):
    # L'appel à markdown est toujours le même donc on instancie
    # le parseur une seule fois pendant toute la durée de vie de l'appli
    parser = markdown.Markdown(safe_mode = 'escape')

    def render(self, text):
        return self.parser.convert(text)
