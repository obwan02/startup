import platform
from startup import operating_systems

script_location = r'H:\ICT\Tools\port_checker.py'

if platform.system() == 'Windows':
    operating_systems.Windows().add(script_location)
