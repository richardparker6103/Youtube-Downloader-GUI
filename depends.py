import os
from clint.textui import progress

pyqt4_link = 'https://ufpr.dl.sourceforge.net/project/pyqt/PyQt4/PyQt-4.10/PyQt4-4.10-gpl-Py2.7-Qt4.8.4-x64.exe'
ffmpeg_link = 'https://ffmpeg.zeranoe.com/builds/win64/static/ffmpeg-20190109-ed3b644-win64-static.zip'

hdr = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
       'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
       'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
       'Accept-Encoding': 'none',
       'Accept-Language': 'en-US,en;q=0.8',
       'Connection': 'keep-alive'}

def download('package'):
        if package == 'ffmpeg':
                file_name = 'ffmpeg.zip'
        r = requests.get(link, stream=True, headers=hdr)
        path = 'ffmpeg.zip'
        with open(path, 'wb') as f:
                total_length = int(r.headers.get('content-length'))
                for chunk in progress.bar(r.iter_content(chunk_size=1024), expected_size=(total_length/1024) + 1): 
                        if chunk:
                                f.write(chunk)
                                f.flush()
                            

