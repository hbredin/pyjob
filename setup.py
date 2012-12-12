#!/usr/bin/env python
# encoding: utf-8

# Copyright 2012 Herve BREDIN (bredin@limsi.fr)

# This file is part of pyjob.
# 
#     pyjob is free software: you can redistribute it and/or modify
#     it under the terms of the GNU General Public License as published by
#     the Free Software Foundation, either version 3 of the License, or
#     (at your option) any later version.
# 
#     pyjob is distributed in the hope that it will be useful,
#     but WITHOUT ANY WARRANTY; without even the implied warranty of
#     MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#     GNU General Public License for more details.
# 
#     You should have received a copy of the GNU General Public License
#     along with pyjob.  If not, see <http://www.gnu.org/licenses/>.


from setuptools import setup, find_packages

setup(
    name='pyjob',
    version='0.1',
    description='Easy job arrays',
    author='Hervé Bredin',
    author_email='bredin@limsi.fr',
    url='https://github.com/hbredin/pyjob',
    packages=['pyjob'],
    package_data={'pyjob': ['templates/qsub.py']},
    install_requires=['numpy >=1.6.1', 
                      'configobj >=4.7.2'],
    classifiers=[ 
       "Development Status :: 4 - Beta", 
       "Intended Audience :: Science/Research", 
       "License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)", 
       "Natural Language :: English", 
       "Programming Language :: Python :: 2.7", 
       "Topic :: Scientific/Engineering"]
)
