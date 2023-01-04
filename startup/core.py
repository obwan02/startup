import platform
from startup import operating_systems

os_startups = { 'Windows': operating_systems.Windows().add, 'Linux': operating_systems.Linux().add }

def add(script_location):
    try:
        os_startups[platform.system()](script_location)
    except KeyError:
        raise NotImplementedError('OS Not Supported')