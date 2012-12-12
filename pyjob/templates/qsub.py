#$ -S $python
#$ -t 1-$grid_size
#$ -N $job_name
#$ -tc $concurrent_jobs
#$ -q $queue
#$ -pe threaded $threads
#$ -V
#$ -o $log_dir
#$ -j y

from pyjob import Grid
from pyjob import CommandTemplate
from pyjob.config import read_configuration_file
import os

# execfile('$config')
_, grid_params = read_configuration_file('$config')

grid_search = Grid(grid_params)
this_job_params = grid_search[int(os.environ['SGE_TASK_ID'])-1]

command = CommandTemplate('$command').substitute(this_job_params)
os.system(command)

