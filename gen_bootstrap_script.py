import virtualenv
import textwrap
output = virtualenv.create_bootstrap_script(textwrap.dedent("""
import os
import subprocess

def after_install(options, home_dir):
    etc = os.path.join(home_dir, 'etc')
    if not os.path.exists(etc):
        os.makedirs(etc)
    subprocess.call([os.path.join(home_dir, 'bin', 'pip'),
                    'install', 'tornado', 'SQLAlchemy', 'MySQL-python'])

def adjust_options(options, args):
    args.append('virtualenv')
    options.use_distribute = True
    options.no_site_packages = True
    options.python = '/usr/bin/python'

"""))
if __name__ == "__main__":
    f = open('bootstrap_fexchange.py', 'w').write(output)
