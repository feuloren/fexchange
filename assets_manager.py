#-*- coding: utf-8 -*-

import os
import os.path
from scss import Scss
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import scss.config as sconf

import logging
logging.getLogger("scss").addHandler(logging.StreamHandler())

class PathException(Exception):
    pass

def compile_file(scss, path, target):
    name, ext = os.path.splitext(os.path.basename(path))
    if ext == '.scss':
        result = scss.compile(scss_file=path)
        with open(os.path.join(target, name+'.css'), 'w') as f:
            f.write(result)

def compile(source, target, compress=False):
    # On regarde si source existe
    # Si target n'existe pas on essaye de le créer
    if not os.path.isdir(source):
        raise PathException(source)
    if not os.path.isdir(target):
        if not os.path.exists(target):
            raise PathException('Not a directory : '+target)
        else:
            try:
                os.makedirs(target)
            except os.error:
                raise Path('Please create directory : '+target)
    
    # on Configure scss (pas terrible comme lib...)
    parser = Scss()
    sconf.LOAD_PATHS += ','+os.path.abspath('assets/frameworks')
    def walker(arg, dirname, names):
        sconf.LOAD_PATHS += ',' + os.path.abspath(dirname)
        for name in names:
            if os.path.isfile(os.path.join(dirname, name)):
                # on compile fichier par fichier
                compile_file(parser, os.path.join(dirname, name), target)
    os.path.walk(source, walker, None)
            
class AssetsHandler(FileSystemEventHandler):
    def __init__(self, source, target, compress):
        super(AssetsHandler, self).__init__()
        self.source = source
        self.target = target
        self.compress = compress

    def on_modified(self, event):
        if event.is_directory:
            return
        # Si un fichier scss a changé on recompile tout
        # car on ne connait pas les relations d'import entre les fichiers
        if event.src_path.endswith('.scss') and not os.path.basename(event.src_path).startswith('.'):
            print os.path.relpath(event.src_path, self.source), 'changed - recompiling assets'
            compile(self.source, self.target, self.compress)

def watch(source, target, compress=False):
    """Observe les modifications des fichiers dans source et relance
    une compilation quand un fichier est modifié
    """
    if not os.path.isdir(source):
        raise PathException(source)
    
    observer = Observer()
    handler = AssetsHandler(source, target, compress)
    observer.schedule(handler, source, True)
    observer.start()
