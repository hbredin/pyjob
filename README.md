pyjob
=====

This Python module eases the process of **qsub**mitting Python job arrays to the cluster.

It is as easy as:

    $ python -m pyjob.grid grid.cfg your_python_script.py %first_param %second_param 

where grid.cfg looks like:

    [ grid ]
    
    # first_param takes values from 0 to 10 with unit step
    first_param = RANGE, 0, 10, 1
    
    # second_param takes values among A, B and C
    second_param = CHOICE, 'A', 'B', 'C'
    
It will launch a job array with all combinations of parameters.

Additionally, you can set **qsub**-related parameters in the configuration file (name of the job array, prefered queue, maximum number of concurrent jobs, etc.)
Just have a look at **sample.cfg** in pyjob/templates to obtain the list of these parameters.

Support for shell scripts should be quite easy to add.
Support for random search in the parameter space could also be added in the future.
