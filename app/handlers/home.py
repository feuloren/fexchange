#!/usr/bin/env python
# -*- coding:utf-8 -*-

from .base import BaseHandler
from ..models import Offre

class HomeHandler(BaseHandler):
    def get(self):
        latest = self.db.query(Offre).filter_by(date_conclusion = None, date_annule = None).order_by(Offre.date_depart).limit(10)
        self.render('home.html', latest=latest)
