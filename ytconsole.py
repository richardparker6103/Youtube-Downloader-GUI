# coding: utf-8

import os, argparse, shutil
import sys, youtube_dl

desktop = os.path.expanduser('~/') + 'Desktop/'
ex = 'https://www.youtube.com/watch?v=C0DPdy98e4c'

def get_info(link):
        try:
                ydl = youtube_dl.YoutubeDL()
                meta = ydl.extract_info(link, download=False)
                #Global titulo, para nome final de arquivo
                global titulo
                titulo = meta['title']
                print '\nTitulo: {}'.format(meta['title'])
                print 'Duracao: {} segundos'.format(meta['duration'])
                print 'Data de upload: {}'.format(meta['upload_date'])
                print 'Uploader: {}'.format(meta['uploader'])
                print 'Visualizacoes: {}'.format(meta['view_count'])
        except TypeError:
                exit("\n[*] Link invalido, impossivel obter informacoes")
		
#get_video_() and get_audio_() downloads content from the web and automatically saves on Desktop, see $desktop
                
def get_video_(link):
        global file_format
        yt = os.system('youtube-dl --format mp4 --output "{}{}.mp4" {}'.format(desktop, titulo, link))
        file_format = '.mp4'
        print "\n[*] {}{} concluido ".format(titulo,file_format)
        
def get_audio_(link):
        global file_format
        yt = os.system('youtube-dl -x --audio-format mp3 --output "{}{}.mp4" {}'.format(desktop, titulo, link))
        file_format = '.mp3'
        print "\n[*] {}{} concluido ".format(titulo,file_format)
        
def send_(device):
        try:
                src_file = desktop + titulo + file_format
                shutil.copy(src_file, device)
                print "[*] {} enviado para {}.".format(src_file, device)
        except IOError:
                print "[*] Nao foi possivel enviar para {}\nveja se o dispositivo esta conectado e tente novamente como administrador.\n".format(device)
        
		
if __name__=="__main__":
        if len(sys.argv) < 2:
                exit("Uso: python ytconsole.py --help")
        parser = argparse.ArgumentParser()
        parser.add_argument("-l", "--link", help='Link do conteudo')
        parser.add_argument('-v', '--video', help='Baixar somente video', action='store_true')
        parser.add_argument('-a', '--audio', help='Baixar somente audio', action='store_true')
        parser.add_argument('-i', '--info', help='Retornar informacoes sobre o link e sair', action='store_true')
        parser.add_argument('-d', '--device', help='Baixar e enviar para dispositivo configurado.', action='store_true')
        args = parser.parse_args()
        link = args.link
        video = args.video
        audio = args.audio
        info = args.info
        device = args.device
        if info:
                get_info(link)
        elif video:
                get_info(link)
                get_video_(link)
                if device:
                        send_(disk_path)
        elif audio:
                get_info(link)
                get_audio_(link)
                if device:
                        send_(disk_path)
                
        
        




		
	
