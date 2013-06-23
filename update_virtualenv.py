#!/bin/env python
# -*- coding:utf-8 -*-

import subprocess
import os.path

try:
    os.environ['VIRTUAL_ENV']
except KeyError:
    print """############
## Attention
## Vous n'êtes pas dans le virtualenv,
## référez vous au fichier README.md pour plus d'informations
############"""
    quit()

class PipManager:
    def __init__(self):
        self.pip = os.path.abspath(os.path.join('virtualenv', 'bin', 'pip'))
        # On récupère la liste des paquest déjà installés
        self.packages = self.get_installed_packages()

    def get_installed_packages(self):
        packages_text = subprocess.check_output([self.pip, 'list', '-l'])
        packages = []
        for package in packages_text.split('\n'):
            name = package.split(' ')[0] # La ligne est de la forme NomDuPackage (version)
            packages.append(name)
        return packages

    def installed(self, package_name):
        return (package_name in self.packages)

    def install(self, package_name):
        subprocess.call([self.pip, 'install', package_name])

def update():
    print '= Mise à jour du virtualenv ='
    dep = open('dependencies', 'r')
    pip = PipManager()
    for package in dep.readlines():
        if package.endswith('\n'):
            package = package[0:-1] # On enlève le \n de fin
        if not pip.installed(package) and package != '':
            print '- Installation de %s -' % package
            pip.install(package)
        else:
            print '- OK : %s -' % package
    dep.close()

if __name__ == '__main__':
    update()
