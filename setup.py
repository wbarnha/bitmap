#!/usr/bin/env python
# coding: utf-8
"""
   File Name: setup.py
      Author: Wan Ji
      E-mail: wanji@live.com
  Created on: Thu May  1 15:24:31 2014 CST
"""
DESCRIPTION = """
"""
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(name='bitmap',
      version='0.0.7',
      author='KX',
      author_email='*',
      package_dir={'bitmap': 'src'},
      packages=['bitmap'],
      url='https://github.com/kx8qt/bitmap',
      # license='LICENSE.txt',
      description='.',
      long_description=open('README.md').read(),
      long_description_content_type="text/markdown",
      classifiers=[
          'Programming Language :: Python :: 3.7',
      ],
      )
