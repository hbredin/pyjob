
from configobj import ConfigObj
from parameter import Range, Choice
from os.path import expanduser

key2param = {'RANGE': Range, 
             'CHOICE': Choice}

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
    grid_params = {}
    for name in config:
         Parameter = key2param[config[name][0]]
         grid_params[name] = Parameter.from_cfg(config[name][1:])
    return grid_params