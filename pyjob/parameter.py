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

import numpy as np

class Choice(object):
    
    @classmethod
    def from_cfg(cls, config):
        return cls(config)
    
    def __init__(self, choices):
        super(Choice, self).__init__()
        assert isinstance(choices, list), \
               "%r is not a list" % choices
        self.choices = choices
    
    def __len__(self):
        return len(self.choices)
    
    def __iter__(self):
        return iter(choices)
    
    def __getitem__(self, key):
        return self.choices[key]

class Range(object):
    
    @classmethod
    def from_cfg(cls, config):
        return cls(config[0], config[1], config[2])
    
    def __init__(self, start, stop, step):
        choices = list(np.arange(start, stop, step))
        super(Range, self).__init__(choices)

