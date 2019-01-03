# -*- coding: cp1252 -*-

import os
import time
import subprocess
import requests
from zipfile import ZipFile
from sys import exit
CREATE_NO_WINDOW = 0x08000000
lst = []

current_dir = os.getcwd()
ffmpeg_link = 'https://ffmpeg.zeranoe.com/builds/win32/static/ffmpeg-20190101-1dcb5b7-win32-static.zip'
youtube_dl_link = 'https://youtube-dl.org/downloads/latest/youtube-dl.exe'

def check_all():
    global x
    try:
        command1 = subprocess.call('ffmpegx -h', creationflags=CREATE_NO_WINDOW)
        print "[*] FFMPEG instalado !"
        time.sleep(0.8)
    except WindowsError:
        print "[*] FFMPEG nao instalado !"
        lst.append('ffmpeg')
    try:
        command2 = subprocess.call('youtube-dlx -h', creationflags=CREATE_NO_WINDOW)
        print "[*] YOUTUBE-DL instalado !"
        time.sleep(0.8)
    except WindowsError:
        print "[*] YOUTUBE-DL nao instalado !"
        lst.append('youtube-dl')
    try:
        import PyQt4
        print "[*] Biblioteca gráfica PyQt4 instalada !"
        time.sleep(0.8)
    except ImportError:
        print "[*] Biblioteca gráfica PyQt4 não instalada ! "
        for x in range(0, 3):
            time.sleep(1.5)
            print "Abrindo em {}...".format(x)
        open_browser = os.system('explorer https://sourceforge.net/projects/pyqt/files/PyQt4/')
        
    if len(lst) == 0:
        exit( "[*] Todas dependencias estao instaladas.")
    else:
        print "[*] Dependencias restantes: \n"
        for x in lst:
            print x
            run('ffmpeg')

        
def run(x):
    if x == 'ffmpeg':
        print "[*] Baixando FFMPEG de {}".format(ffmpeg_link)
        print "[*] Por favor, aguarde..."
        r = requests.get(ffmpeg_link, allow_redirects=True)
        open('ffmpeg.zip', 'wb').write(r.content)
        z = ZipFile('ffmpeg.zip')
        z.extractall()
        print "[*] FFMPEG extraido, copiando arquivos no diretorio principal..."
        os.system("move ffmpeg-20190101-1dcb5b7-win32-static\bin\*.exe") 
        print "[*] FFMPEG instalado com sucesso !"
        os.system('del ffmpeg.zip')
        os.system('rmdir ffmpeg-20190101-1dcb5b7-win32-static /S /Q')
        exit()
    if x == 'youtube-dl':
        print "[*] Baixando YOUTUBE-DL de {}".format(youtube_dl_link)
        print "[*] Por favor, aguarde..."
        try:
            ydl = requests.get(youtube_dl_link, allow_redirects=True)
        except ConnectionError:
            exit ("[*] O servidor esta inapto a responder as requests ERRO HTTPS[10060]")
        open('youtube-dl.exe', 'wb').write(ydl.content)
        print "[*] YOUTUBE-DL instalado com sucesso !"
        
check_all()


    
    


        
