#!/usr/bin/env python
# encoding: utf-8

from setuptools import setup, find_packages

setup(
    name='pyjob',
    version='0.1',
    description='Easy job arrays',
    author='Hervé Bredin',
    author_email='bredin@limsi.fr',
    url='https://github.com/hbredin/pyjob',
    # packages= find_packages(),
    packages=['pyjob'],
    package_data={'pyjob': ['templates/qsub.py']},
    install_requires=['numpy >=1.6.1', ],
    classifiers=[ 
       "Development Status :: 4 - Beta", 
       "Intended Audience :: Science/Research", 
       "License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)", 
       "Natural Language :: English", 
       "Programming Language :: Python :: 2.7", 
       "Topic :: Scientific/Engineering"]
)
