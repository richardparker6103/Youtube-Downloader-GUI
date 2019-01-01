# -*- coding: utf-8 -*-

import os
import argparse
import sys

pasta_local = os.path.expanduser('~/') + 'Desktop/'
disk_path = 'E:/'

def baixar_video(link):
    yt = os.system('youtube-dl --format mp4 %s' % link)
def baixar_audio(link):
    yt = os.system('youtube-dl -x --audio-format mp3 %s' % link)
def enviar(destino):
    if metodo == 'audio':
        cp = os.system('move *.mp3 %s' %destino)
        if cp == 1:
            exit('\n[*]O arquivo nao pode ser enviado\n')
        print 'Arquivo enviado para %s'
    else:
        cp = os.system('move *.mp4 %s' %destino)
        if cp == 1:
            exit('\n[*]O arquivo nao pode ser enviado\n')
        print 'Arquivo enviado para %s' % destino
		
if __name__=="__main__":
    if len(sys.argv) < 2:
        exit("Uso: os2.py -l https://youtube.com/watch?video=7876asxXa87s")
    parser = argparse.ArgumentParser(prog="os2.py", usage="os2.py -l [YOUTUBE_LINK]")
    parser.add_argument("-l", "--link", help='selecione o link do video')
    parser.add_argument('-v', '--video', help='baixar somente video', action='store_true')
    parser.add_argument('-a', '--audio', help='baixar somente audio', action='store_true')
    parser.add_argument('-p', '--pendrive', help='direto pro pendrive', action='store_true')
    args = parser.parse_args()
    pendrive = args.pendrive
    link = args.link
    video = args.video
    audio = args.audio
    
    if video:
        metodo = 'video'
        baixar_video(link)
        if pendrive:
            enviar(disk_path)
        else:
            enviar(pasta_local)
    if audio:
        metodo = 'audio'
        baixar_audio(link)
        if pendrive:
            enviar(disk_path)
        else:
            enviar(pasta_local)

		
	
