try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'Solver',
    'author': 'Clayton',
    'url': 'http://www.github.com/notyalc/PySolver',
    'download_url': 'http://www.github.com/notyalc/PySolver.git',
    'author_email': 'git_notyalc@gmail.com',
    'version': '0.1',
    'install_requires': ['nose'],
    'packages': ['NAME'],
    'scripts': [],
    'name': 'projectname'
}

setup(**config)