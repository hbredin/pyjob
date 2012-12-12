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

import sys, os
from tempfile import mkstemp
import pkg_resources
from template import QSubTemplate
import subprocess

class Grid(object):
    
    def __init__(self, params):
        super(Grid, self).__init__()
        self.params = params
    
    def __len__(self):
        nCombinations = 1
        for name, param in self.params.iteritems():
            nCombinations = nCombinations * len(param)
        return nCombinations
    
    def __getitem__(self, key):
        combination = {}
        nCombinations = len(self)
        for name, param in self.params.iteritems():
            nCombinations = nCombinations/len(param)
            n = key / nCombinations
            combination[name] = param[n]
            key = key % nCombinations
        return combination
    
    def __iter__(self):
        for n in range(len(self)):
            yield self[n]

if __name__ == "__main__":
    
    # read configuration file
    config = sys.argv[1]
    execfile(config)
    if 'queue' not in qsub_params:
        qsub_params['queue'] = 'all.q'
    if 'job_name' not in qsub_params:
        qsub_params['job_name'] = 'my_job'
    if 'concurrent_jobs' not in qsub_params:
        qsub_params['concurrent_jobs'] = 20
    if 'threads' not in qsub_params:
        qsub_params['threads'] = 1
    # TODO -- replace by this below:
    # grid_params, qsub_params = read_configuration_file(config)
    
    qsub_params['python'] = sys.executable
    qsub_params['config'] = sys.argv[1]
    qsub_params['command'] = " ".join(sys.argv[2:])
    
    # generate parameter grid
    grid = Grid(grid_params)
    
    qsub_params['grid_size'] = len(grid)
    
    # load qsub.py template as a string
    path = pkg_resources.resource_filename('pyjob', 'templates/qsub.py')
    with open(path, 'r') as f:
        qsub_py = f.read()
    qsubTemplate = QSubTemplate(qsub_py)
    
    # fill template and create a temporary qsubable file
    qsub_py = qsubTemplate.safe_substitute(qsub_params)
    fd, path = mkstemp(suffix='.py', prefix='qsub', dir=None, text=True)
    with os.fdopen(fd, 'w') as f:
        f.write(qsub_py)
    
    # submit the job
    qsub_msg = subprocess.check_output(['qsub',path])
    print qsub_msg
    