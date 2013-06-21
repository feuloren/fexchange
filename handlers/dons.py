#!/usr/bin/env python
# -*- coding:utf-8 -*-

from .base import BaseHandler
from models import Don

class DonsHandler(BaseHandler):
    def get(self):
        dons = self.db.query(Don).filter_by(date_conclusion = None, date_annule = None).limit(20)
        self.render('dons/index.html', dons=dons)
