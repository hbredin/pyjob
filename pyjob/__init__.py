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

"""
python -m pyjob.grid config.py command args
"""


__date__ = ''
__author__ = 'Herve Bredin <bredin@limsi.fr>'
__version__ = '0.1'

from grid import Grid
from parameter import Choices, Range

if __name__ == '__main__':
    import doctest
    doctest.testmod()