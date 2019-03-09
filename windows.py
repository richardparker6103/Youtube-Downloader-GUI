import os

_dir_ = os.getcwd()

os.system('pip install pyinstaller')
os.system('pyinstaller --noconsole --onefile -i ytbico.ico ytdown.py')
os.system('copy dist/ytdown.py {}'.format(str(dir) + '/'))
print '[*] Executavel criado.'
