import time, os, requests, zipfile
from clint.textui import progress

pyqt4_link = 'https://ufpr.dl.sourceforge.net/project/pyqt/PyQt4/PyQt-4.10/PyQt4-4.10-gpl-Py2.7-Qt4.8.4-x64.exe'
ffmpeg_link = 'https://ffmpeg.zeranoe.com/builds/win64/static/ffmpeg-20190109-ed3b644-win64-static.zip'

#Headers ( evita o erro 403 Forbidden )
hdr = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
       'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
       'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
       'Accept-Encoding': 'none',
       'Accept-Language': 'en-US,en;q=0.8',
       'Connection': 'keep-alive'}

def download_pkg(package):
        if package == 'ffmpeg':
                file_name = 'ffmpeg.zip'
                link = ffmpeg_link
        else:
                file_name = 'pyqt4.exe'
                link = pyqt4_link
        r = requests.get(link, stream=True, headers=hdr)

        with open(file_name, 'wb') as f:
                total_length = int(r.headers.get('content-length'))
                for chunk in progress.bar(r.iter_content(chunk_size=1024), expected_size=(total_length/1024) + 1): 
                        if chunk:
                                f.write(chunk)
                                f.flush()
                            
def extract_():
        with zipfile.ZipFile('ffmpeg.zip', 'r') as zip_ref:
                zip_ref.extractall('ffmpeg')                
                print "[*] Extraindo ffmpeg, aguarde ..."
                time.sleep(4)    

def main():
        
        fc = os.system('ffmpeg -h > NUL')
        if fc == 1:
               if os.path.isfile('ffmpeg.zip') == True:
                       print "[*] zip file encontrado !"
                       extract_()
                       time.sleep(3)
                       print '[*] Concluido.'
               else:
                       download_pkg('ffmpeg')
                       extract_()
                        
        else:
               print '[*] FFmpeg encontrado .'
               pass
       
        try:
               import PyQt4
        except ImportError:
               print "[*] PyQt4 nao instalado, baixando..."
               time.sleep(3)
               download_pkg('pyqt4')
               print '[*] Concluido'
               time.sleep(3)
               os.system('pyqt4.exe')

main()
       
       
