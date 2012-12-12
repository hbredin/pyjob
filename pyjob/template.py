from string import Template

class CommandTemplate(Template):
    delimiter = '%'
    def __init__(self, command):
        super(CommandTemplate, self).__init__(command)

class QSubTemplate(Template):
    delimiter = '$'
    def __init__(self, qsub_py):
        super(QSubTemplate, self).__init__(qsub_py)

