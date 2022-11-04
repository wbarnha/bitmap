#!/usr/bin/env python
# coding: utf-8
"""
   File Name: setup.py
      Author: Wan Ji
      E-mail: wanji@live.com
  Created on: Thu May  1 15:24:31 2014 CST
"""
DESCRIPTION = """
An updated version of the bitmap library from https://github.com/wanji/bitmap
"""
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(name='bitmap2',
      use_scm_version=True,
      setup_requires=['setuptools_scm'],
      author='wbarnha',
      author_email='williambbarnhart@gmail.com',
      package_dir={'bitmap': 'src'},
      packages=['bitmap'],
      url='https://github.com/wbarnha/bitmap',
      license='LICENSE.txt',
      description=DESCRIPTION,
      long_description=open('README.md').read(),
      long_description_content_type="text/markdown",
      classifiers=[
            'Programming Language :: Python :: 2.7',
            'Programming Language :: Python :: 3',
            'Topic :: Utilities',
            'License :: OSI Approved :: MIT License',
            'Development Status :: 5 - Production/Stable',
            'Intended Audience :: Developers',
      ],
      )
