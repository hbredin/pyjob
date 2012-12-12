#$ -S $python
#$ -t 1-$grid_size
#$ -N $job_name
#$ -tc $concurrent_jobs
#$ -q $queue
#$ -pe threaded $threads
#$ -V
#$ -o $log_dir
#$ -j y

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

from pyjob import Grid
from pyjob import CommandTemplate
from pyjob.config import read_configuration_file
import os

_, grid_params = read_configuration_file('$config')

grid_search = Grid(grid_params)
this_job_params = grid_search[int(os.environ['SGE_TASK_ID'])-1]

command = CommandTemplate('$command').substitute(this_job_params)
os.system(command)

