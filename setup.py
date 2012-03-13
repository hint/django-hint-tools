#!/usr/bin/env python

from distutils.core import setup
import glob

setup(name='django-centralniak-tools',
      version='0.1',
      description='Package of handy django console tools',
      author='Piotr Kilczuk',
      author_email='p.kilczuk@neumea.pl',
      url='https://github.com/centralniak/django-centralniak-tools',
      scripts=glob.glob('scripts/*')
)