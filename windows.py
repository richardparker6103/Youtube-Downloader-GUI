import os

_dir_ = os.getcwd()

os.system('pip install pyinstaller')
os.system('pyinstaller --noconsole --onefile -i ytbico.ico ytdown.py')
os.system('copy dist/ytdown.py {}'.format(dir + '/'))
print '[*] Executavel criado.'