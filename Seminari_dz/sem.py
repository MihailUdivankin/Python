pip install pathlib

# PS C:\Users\User\Documents\Python> pip install pathlib
# Collecting pathlib
#   Downloading pathlib-1.0.1-py3-none-any.whl (14 kB)
# Installing collected packages: pathlib
# Successfully installed pathlib-1.0.1
# WARNING: You are using pip version 22.0.4; however, version 22.2 is available.
# You should consider upgrading via the 
# 'C:\Users\User\AppData\Local\Microsoft\WindowsApps\PythonSoftwareFoundation.Python.3.10_qbz5n2kfra8p0\python.exe -m pip install --upgrade pip' command.


# pip install pathlib  # установка модуля pathlib

import pathlib # подключение модуля pathlib
from pathlib import Path # подключение модуля pathlib

dir_path = pathlib.Path.cwd() #Получаем строку, содержащую путь к рабочей директории:
print(dir_path)
# dir_path = pathlib.Path.home() #Получаем строку, содержащую путь к домашней директории:
# print(dir_path)