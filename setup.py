#!/usr/bin/env python

from setuptools import setup

setup(name='Asadetris',
      version='0.1',
      description='A simple tetris like game.',
      author='Losersjuegos',
      author_email='hugoruscitti@gmail.com',
      url='http://www.losersjuegos.com.ar',
      packages=['lib'],
      install_requires=['pygame'],
      scripts=['asadetris'],
     )

