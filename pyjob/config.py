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

from configobj import ConfigObj
from parameter import Range, Choice, FileContent, UniqueValue
from os.path import expanduser

key2param = {'RANGE': Range, 
             'CHOICE': Choice,
             'FILE': FileContent,
             'VALUE': UniqueValue,
             }

def read_configuration_file(filename):
    config = ConfigObj(filename)
    qsub_params = get_qsub_params(config['qsub'])
    grid_params = get_grid_params(config['grid'])
    return qsub_params, grid_params

def get_qsub_params(config):
    
    qsub_params = {'concurrent_jobs': 20,
                   'threads': 1,
                   'queue': 'all.q',
                   'log_dir': expanduser('~'),}
    for name in config:
        if name == 'concurrent_jobs':
            qsub_params[name] = int(config[name])
        elif name == 'threads':
            qsub_params[name] = int(config[name])
        elif name == 'queue':
            qsub_params[name] = str(config[name])
        elif name == 'job_name':
            qsub_params[name] = str(config[name])
        elif name == 'log_dir':
            qsub_params[name] = str(config[name])
        else:
            qsub_params[name] = config[name]
    
    return qsub_params

def get_grid_params(config):
    """
    Parameters
    ----------
    config : dict
        {param: list} dictionary (e.g. 'alpha': ['RANGE', '0', '10', '1'])
    
    Returns
    -------
    grid : dict
        {param: Parameter instance} dictionary (e.g. 'alpha': Range(0,10,1))
    """
    grid_params = {}
    for name in config:
         Parameter = key2param[config[name][0]]
         grid_params[name] = Parameter.from_cfg(config[name][1:])
    return grid_params