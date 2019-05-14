**Windows**
Registry Changes:
 - Key added at HKCU:Software\Microsoft\Windows\CurrentVersion\Run
 - Name is `python_startup_lib` with value of generated batch file

File Changes:
 - Folder made at "C:\Users\%username%\AppData\Local\programs\python_startup_lib"
 - Bat file made inside this folder called `win_startup.bat`