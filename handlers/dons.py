#!/usr/bin/env python
# -*- coding:utf-8 -*-

from .base import BaseHandler
from models import Offre

class DonsHandler(BaseHandler):
    def get(self):
        dons = self.db.query(Offre).filter_by(type = 'don', date_conclusion = None, date_annule = None).limit(20)
        self.render('dons/index.html', dons=dons)
