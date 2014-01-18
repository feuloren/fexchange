#!/usr/bin/env python
# -*- coding:utf-8 -*-

from pytest import fail
from selenium import webdriver
from selenium.webdriver.common.by import By

# Doc pour le webdriver :
#http://selenium.googlecode.com/git/docs/api/py/webdriver_remote/selenium.webdriver.remote.webdriver.html
# Et pour les webelement obtenus par un find_element :
#http://selenium.googlecode.com/git/docs/api/py/webdriver_remote/selenium.webdriver.remote.webelement.html#module-selenium.webdriver.remote.webelement

class TestComptesUtilisateur:
    def setup(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)

    def teardown(self):
        self.browser.quit()

    def test_connexion_cas(self):
        self.browser.get('http://localhost:8888')
        assert 'Adopte un meuble' in self.browser.title

        # On veut s'authentifier avec le CAS
        # d'abord on va sur la page de connexion
        link = self.browser.find_element(By.LINK_TEXT, 'Connexion')
        link.click()
        assert self.browser.current_url == 'http://localhost:8888/auth'

        assert 'Connexion' in self.browser.title

        fail('Finish the test !')

