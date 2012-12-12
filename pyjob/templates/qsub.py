#$ -S $python
#$ -t 1-$grid_size
#$ -N $job_name
#$ -tc $concurrent_jobs
#$ -q $queue
#$ -pe threaded $threads
#$ -V

from pyjob import Grid
from pyjob import CommandTemplate

execfile('$config')
grid_search = Grid(grid_params)
this_job_params = grid_search[int(os.environ['SGE_TASK_ID'])]
os.system(CommandTemplate('$command').substitute(this_job_params))
