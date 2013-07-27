# -*- coding:utf-8 -*-

from tornado.web import URLSpec as route
from handlers import *

routes = [
    route(r"/", HomeHandler),
    route(r"/recherche(?:/(.*))?", RechercheHandler),
    route(r"/ajouter/vente", NewVenteHandler, name='nouvelle_vente'),
    route(r"/ajouter/pret", NewPretHandler, name='nouveau_pret'),
    route(r"/ajouter/don", NewDonHandler, name='nouveau_don'),
    route(r"/vente/(\d+)", ShowVenteHandler, name='show_vente'),
    route(r"/auth", LoginHandler, name='login'),
    route(r"/auth/logout", LogoutHandler, name='logout'),
    route(r"/auth/cas", CasHandler, name='cas_auth'),
    route(r"/auth/cas/register", CasRegisterHandler, name='cas_register'),
    route(r"/auth/classic", PasswordAuthHandler),
    route(r"/auth/register", RegisterHandler, name='register'),
]
