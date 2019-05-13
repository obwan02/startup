import platform
import os
from startup import template

# Windows imports
if platform.system() == 'Windows':
    import winreg

class Windows(template.StartupTemplate):
    def __init__(self):
        super().__init__()
        
        self.library_home = os.path.join(os.getenv('LOCALAPPDATA'), r'programs\python_startup_lib')
        if not os.path.exists(self.library_home):
            os.makedirs(self.library_home)

        self.bat_location = os.path.join(self.library_home, r'win_startup.bat')

    def bat_append(self, script_location):
        ''' Add to window's launch script '''
        with open(self.bat_location, 'a+') as f:
            if script_location not in f.read():
                f.write('\n & "{}" "{}"'.format(self.python_location, script_location))

    def add(self, script_location):
        ''' Add script to startup '''
        self.bat_append(script_location)

        reg = winreg.OpenKey(winreg.HKEY_CURRENT_USER,r'Software\Microsoft\Windows\CurrentVersion\Run',0, winreg.KEY_ALL_ACCESS)
        with reg:
            var_type = winreg.REG_SZ
            if '%' in self.bat_location:
                var_type = winreg.REG_EXPAND_SZ
            winreg.SetValueEx(reg, 'python_startup_lib', 0, var_type, self.bat_location)