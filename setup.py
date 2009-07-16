#!/usr/bin/env python

from distutils.core import setup

setup(name='Asadetris',
      version='0.1',
      description='A simple tetris like game.',
      author='Losersjuegos',
      author_email='hugoruscitti@gmail.com',
      url='http://www.losersjuegos.com.ar',
      packages=['lib'],

      #package_dir={'lib': 'images'},
      #package_data={'lib': ['images/*']},
      #data_files=[('bitmaps', ['images'])],
      scripts=['asadetris'],
     )

