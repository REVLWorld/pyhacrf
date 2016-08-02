import sys
from setuptools import setup, Extension
from codecs import open
from os import path


# from Michael Hoffman's http://www.ebi.ac.uk/~hoffman/software/sunflower/
class NumpyExtension(Extension):

    def __init__(self, *args, **kwargs):
        from numpy import get_include
        from numpy.distutils.misc_util import get_info
        kwargs.update(get_info('npymath'))
        kwargs['include_dirs'] += [get_include()]

        Extension.__init__(self, *args, **kwargs)

here = path.abspath(path.dirname(__file__))


# Get the long description from the relevant file
with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()


def setup_package():
    setup_args = {
        "name": 'pyhacrf-datamade',
        "version": '0.2.0',
        "packages": ['pyhacrf'],
        "install_requires": ['numpy>=1.9', 'PyLBFGS>=0.1.3'],
        "setup_requires": ['numpy'],
        "url": 'https://github.com/dirko/pyhacrf',
        "download_url": 'https://github.com/datamade/pyhacrf',
        "author": 'Dirko Coetsee',
        "author_email": 'dpcoetsee@gmail.com',
        'maintainer': 'Forest Gregg',
        'maintiner_email': 'fgregg@gmail.com',
        "description": 'Hidden alignment conditional random field, a discriminative string edit distance',
        "long_description": long_description,
        "classifiers": [
            'Intended Audience : : Science/Research',
            'License : : OSI Approved :: BSD License',
            'Operating System : : OS Independent',
            'Programming Language : : Python',
            'Topic : : Scientific/Engineering',
        ],
    }

    def is_special_command():
        if len(sys.argv) < 2:
            return False

        special_list = ('--help-commands',
                        'egg_info',
                        '--version',
                        'clean')
        return ('--help' in sys.argv[1:] or
                sys.argv[1] in special_list)

    if not is_special_command():
        setup_args['ext_modules'] = [
            NumpyExtension('pyhacrf.algorithms', 
                           ['pyhacrf/algorithms.c'],
                           extra_compile_args = ["-ffast-math", "-O4"]),
            NumpyExtension('pyhacrf.adjacent', 
                           ['pyhacrf/adjacent.c'],
                           extra_compile_args = ["-ffast-math", "-O4"]),
        ]

    setup(**setup_args)

if __name__ == "__main__":
    setup_package()
