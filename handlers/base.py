# -*- coding:utf-8 -*-

import tornado.web

class BaseHandler(tornado.web.RequestHandler):
    @property
    def db(self):
        return self.application.db

    def get_current_user(self):
        user_id = self.get_secure_cookie("user")
        if not user_id: return None
        return self.db.query(User).get(user_id)

    def static_url(self, filename):
        """On stocke nos fichiers statiques sous un autre domaine.
        et on n'a pas besoin du versionnage des fichiers"""
        self.require_setting("static_path", "static_host")
        
        if self.application.settings['debug']:
            """en mode debug on sert le fichiers en local"""
            return '/static/' + filename
        else:
            """en mode production il faut qu'ils soit publiés"""
            return self.application.settings["static_host"] + filename
