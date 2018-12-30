# -*- coding: cp1252 -*-
#------------------README-------------------------
# Necessário executáveis ffmpeg, ffprobe, ffplay 
# Por falta de espaço do github, é necessário baixar manualmente os componentes no site:
# FFMPEG -> (ffmpeg, ffplay, ffprobe) https://www.ffmpeg.org/download.html
# LIBAV -> (para evitar conflitos com o ffmpeg)
# youtube-dl.exe(para download e conversão dos arquivos) -> https://youtube-dl.org/
# PyQt biblioteca para edição GUI -> https://sourceforge.net/projects/pyqt/files/PyQt4/
#------------------README-------------------------
# Required executable ffmpeg, ffprobe, ffplay!
# For lack of space of github, is to download the media components on the site:
# FFMPEG -> (ffmpeg, ffplay, ffprobe) https://www.ffmpeg.org/download.html
# LIBAV -> (to avoid with ffmpeg)
# youtube-dl.exe (for download and file conversion) -> https://youtube-dl.org/
# PyQt library for GUI editing -> https://sourceforge.net/projects/pyqt/files/PyQt4/
#--------------------------------------------------


import sys
import os
import subprocess
import mimetypes
import time
from os2 import *
from PyQt4.QtCore import *
from PyQt4.QtGui import *

l = []
    

#Hide output console while downloading
si = subprocess.STARTUPINFO()
si.dwFlags |= subprocess.STARTF_USESHOWWINDOW
CREATE_NO_WINDOW = 0x08000000

example = 'https://www.youtube.com/watch?v=C0DPdy98e4c'
x = 1
local_path = os.getcwd()

    
class Window(QMainWindow):
        def __init__(self):
                super(Window, self).__init__()
                self.setGeometry(50,50,700,500)
                self.setWindowTitle('Python Youtube Downloader')
                self.setWindowIcon(QIcon('ytbico.ico'))                   
                extractAction = QAction("Abrir arquivo de texto", self)
                extractAction.setShortcut("Ctrl+Q")
                extractAction.setStatusTip('Ler varios objetos a partir de um arquivo de texto')
                extractAction.triggered.connect(self.browse)
                mainMenu = self.menuBar()
                fileMenu = mainMenu.addMenu('Arquivo')
                fileMenu.addAction(extractAction)
                self.home()
        def home(self):
            global tipo
            self.pic = QLabel(self)
            self.pic.setPixmap(QPixmap('ytbico.ico'))
            self.pic.setGeometry(234,-100,480,480)
            self.button = QPushButton('Somente vídeo', self)
            self.button.clicked.connect(self.iniciar_video)
            self.button.resize(100,30)
            self.button.move(260,300)
            self.button2 = QPushButton('Somente áudio', self)
            self.button2.clicked.connect(self.iniciar_audio)
            self.button2.move(380,300)
            self.button4 = QPushButton('Baixar em dispositivo', self)
            self.button4.clicked.connect(self.iniciar_audio_pendrive)
            self.button4.resize(130,30)
            self.button4.move(305,350)
            self.button5 = QPushButton('Selecionar arquivo...', self)
            self.button5.clicked.connect(self.browse_convert)
            self.button5.resize(121,30)
            self.button5.move(30,420)
            self.button6 = QPushButton('Iniciar', self)
            self.button6.clicked.connect(self.iniciar_conversao)
            self.button6.resize(60,40)
            self.button6.move(600,420)
            self.textbox = QLineEdit(self)
            self.textbox.move(227, 265)
            self.textbox.resize(280,25)
            self.avi = QCheckBox('AVI', self)
            self.avi.setGeometry(QRect(500,420,71,21))
            self.wmv = QCheckBox('WMV', self)
            self.wmv.setGeometry(QRect(500,440,71,21))
            self.mov = QCheckBox('MOV', self)
            self.mov.setGeometry(QRect(500,460, 71,21))
            self.mkv = QCheckBox('MKV', self)
            self.mkv.setGeometry(QRect(500,400, 71,21))
            self.aac = QCheckBox('AAC', self)
            self.aac.setGeometry(QRect(300, 400, 71,21))
            self.wma = QCheckBox('WMA', self)
            self.wma.setGeometry(QRect(300, 420, 71,21))
            self.flac = QCheckBox('FLAC', self)
            self.flac.setGeometry(QRect(300, 440, 71,21))
            self.progress = QProgressBar(self)
            self.progress.setGeometry(0, 480, 735, 20)
            self.tx = QLabel("Insira a URL ->", self)
            self.tx.move(120,265)
            self.tx.setFont(QFont('Monospace', 11))
            self.tx2 = QLabel("Converter para: ", self)
            self.tx2.move(400,420)
            self.tx3 = QLabel("Converter para: ", self)
            self.tx3.move(200,420)
            self.linha1 = QLabel('_____________________________________________________________________________________________________________________', self)
            self.linha1.move(0, 230)
            self.linha1.resize(1000, 20)
            self.linha2 = QLabel('_____________________________________________________________________________________________________________________', self)
            self.linha2.move(0, 375)
            self.linha2.resize(1000, 20)
            self.show()
                
        def iniciar_video(self, estado='normal', lista='False'):
                global link
                if lista == 'True':
                    link = k
                    subprocess.call('python os2.py -v -l %s' %link, creationflags=CREATE_NO_WINDOW)
                else:
                    link = self.textbox.text()
                    if len(link) < 40:
                        self.msg = QMessageBox()
                        self.msg.setIcon(QMessageBox.Information)
                        self.msg.setText("O link '{}' é invalido, por favor digite novamente.".format(str(link)))
                        self.msg.setWindowTitle('Python Youtube Downloader')
                        self.msg.setWindowIcon(QIcon('ytbico.ico'))
                        self.msg.exec_()
                    else:
                        self.completed = 0
                        subprocess.call('python os2.py -v -l %s' %link, creationflags=CREATE_NO_WINDOW)
                        if lista == 'False':
                            while self.completed < 100:
                                self.completed += 0.0001
                                self.progress.setValue(self.completed)
                            self.msg = QMessageBox()
                            self.msg.setIcon(QMessageBox.Information)
                            self.msg.setText("Vídeo salvo na área de trabalho")
                            self.msg.setWindowTitle('Python Youtube Downloader')
                            self.msg.setWindowIcon(QIcon('ytbico.ico'))
                            self.msg.exec_()                                  
                        else:
                            pass      
                     
        def iniciar_audio_pendrive(self):
                link = self.textbox.text()
                try:
                    s = os.chdir('E:/')
                    os.chdir(local_path)
                    subprocess.call('python os2.py -a -p -l %s' %link, creationflags=CREATE_NO_WINDOW)
                    self.completed = 10
                    while self.completed < 100:
                            self.completed += 0.0001
                            self.progress.setValue(self.completed)
                    self.msg = QMessageBox()
                    self.msg.setIcon(QMessageBox.Information)
                    self.msg.setWindowTitle('Python Youtube Downloader')
                    self.msg.setText("O arquivo MP3 foi salvo no pendrive E:/")
                    self.msg.setWindowIcon(QIcon('ytbico.ico'))
                    self.msg.exec_()                     
                except WindowsError:
                    global x
                    x = x + 1
                    self.msg2 = QMessageBox()
                    self.msg2.setIcon(QMessageBox.Information)
                    self.msg2.setWindowTitle('Python Youtube Downloader')
                    self.msg2.setText('Pendrive desconectado, conecte e tente novamente.')
                    self.msg2.setWindowIcon(QIcon('ytbico.ico'))
                    self.msg2.exec_()
                    
                

                
        def iniciar_audio(self, estado='normal', lista='False'):
                if lista == 'True':
                    link = k
                    if estado == 'pnd':
                        subprocess.call('python os2.py -a -p -l %s' %link, creationflags=CREATE_NO_WINDOW)
                    else:
                        subprocess.call('python os2.py -a -l %s' %link, creationflags=CREATE_NO_WINDOW)
                else:
                    link = self.textbox.text()
                    if len(link) < 40:
                        self.msg = QMessageBox()
                        self.msg.setIcon(QMessageBox.Information)
                        self.msg.setText("O link '{}' inválido, por favor, digite um link valido.".format(str(link)))
                        self.msg.setWindowTitle('Python Youtube Downloader')
                        self.msg.setWindowIcon(QIcon('ytbico.ico'))
                        self.msg.show()
                    else:
                        self.completed = 0
                        subprocess.call('python os2.py -a -l %s' %link, creationflags=CREATE_NO_WINDOW)
                        if lista == 'False':
                            while self.completed < 100:
                                self.completed += 0.0001
                                self.progress.setValue(self.completed)
                            self.msg = QMessageBox()
                            self.msg.setIcon(QMessageBox.Information)
                            self.msg.setText("Vídeo salvo na área de trabalho")
                            self.msg.setWindowTitle('Python Youtube Downloader')
                            self.msg.setWindowIcon(QIcon('ytbico.ico'))
                            self.msg.exec_()                                  
                        else:
                            pass                    

        def iniciar_conversao(self):
            if self.avi.isChecked():
                tipo = 'avi'
            elif self.wmv.isChecked():
                tipo = 'wmv'
            elif self.mov.isChecked():
                tipo = 'mov'
            elif self.mkv.isChecked():
                tipo = 'mkv'
            elif self.aac.isChecked():
                tipo = 'aac'
            elif self.wma.isChecked():
                 tipo = 'wma'
            elif self.flac.isChecked():
                tipo = 'flac'
            f = file(str(source_arquivo))
            f2 = f.name.split('.')
            source_formato = f2[1]
            print 'Arquivo inicial : ' + source_arquivo + '\nFormato inicial ----> ' + tipo + '\nFormato final ---->' + source_formato
            self.msg = QMessageBox()
            self.msg.setIcon(QMessageBox.Information)
            self.msg.setText("A seguir, escolha um nome para seu arquivo.")
            self.msg.setWindowTitle('Python Youtube Downloader')
            self.msg.setWindowIcon(QIcon('ytbico.ico'))
            self.msg.exec_()
            arquivo_final = QFileDialog.getSaveFileName(self, 'Save File')
            asp = QMessageBox.question(Window(), 'Deseja prosseguir ?',  'Arquivo: {}\nFormato inicial: {}\nFormato final: {}'
                                       .format(str(source_arquivo),str(source_formato), str(tipo)), QMessageBox.Yes, QMessageBox.No)
            if asp == QMessageBox.Yes:
                print tipo
                if tipo == 'avi' or tipo == 'mkv' or tipo == 'wmv' or tipo == 'mov':
                    #The '"{}"' bypass windows error by space ( O código '"{}"' faz com que o windows não bugue na hora de encontrar o arquivo e pasta como nomes separados, ex : "C:\Users\Video de luta.mp4"
                    source_arquivo_final = '"{}"'.format(source_arquivo)
                    print source_arquivo_final
                    print tipo
                    print arquivo_final + '.' + tipo
                    convert_command = 'ffmpeg -i {} {}'.format(str(source_arquivo_final), str(arquivo_final + '.' + tipo))
                    os.system(convert_command)
                elif tipo == 'aac' or tipo == 'flac' or tipo == 'wma':
                    source_arquivo_final = '"{}"'.format(source_arquivo)
                    print source_arquivo
                    print tipo
                    print arquivo_final + '.' + tipo
                    convert_command = 'ffmpeg -i {} {}'.format(str(source_arquivo_final), str(arquivo_final + '.' + tipo))
                    os.system(convert_command)
                #continue
                    
                
            #if tipo == False:
              #  self.msg = QMessageBox()
                #self.msg.setIcon(QMessageBox.Information)
                #self.msg.setText("Selecione o arquivo e escolha o formato desejado !")
                #self.msg.setWindowTitle('Python Youtube Downloader')
                #self.msg.setWindowIcon(QIcon('ytbico.ico'))
                #self.msg.show()
            #else:
             #   print 'Formato de arquivo: %s' %tipo
             #   exit()
             #   if tipo=='video':
             #       convert_command = 'ffmpeg -i {} -b:v 16M -vcodec h264 -acodec aac -strict -2 {}'.format(str(arquivo), str(destino))
             #   else:
              #      convert_command = 'ffmpeg -i {} -b:a 16M -acodec libmp3lame {}'.format(str(arquivo), str(destino))
                
            
        def browse_convert(self):
            global x
            x += 1
            #Clear the content before repeat ( limpa o conteudo da variável self.tx5 antes de preencher outra em caso de erro do usuario )
            if x >= 3:
                self.tx5.clear()
            global source_arquivo
            time.sleep(1)
            source_arquivo = QFileDialog.getOpenFileName()
            print 'Arquivo selecionado -->' + source_arquivo + '\n'
            self.tx5 = QLabel(source_arquivo, self)
            #Resize for increase the text ( redimensionar o tamanho para aparecer todo o conteúdo do texto )
            self.tx5.resize(400,20)
            self.tx5.move(15,455)
            self.tx5.setFont(QFont('Monospace', 9))
            self.tx5.show()
            
            


        def browse(self, convert=False):
            global k
            nome_arquivo = QFileDialog.getOpenFileName()
            print 'filePath' + nome_arquivo + '\n'
            fileHandle = open(nome_arquivo, 'r')
            if ".txt" in nome_arquivo:
                print "É TXT"
            else:
                print "NAO E TXT\n ALERTANDO..."
                self.msgt = QMessageBox()
                self.msgt.setIcon(QMessageBox.Information)
                self.msgt.setWindowTitle('Python Youtube Downloader')
                self.msgt.setText("O arquivo {} selecionado não é valido, selecione um arquivo em formato .txt".format(str(nome_arquivo)))
                self.msgt.setWindowIcon(QIcon('ytbico.ico'))
                self.msgt.exec_()
                self.browse()
                            
            lines = fileHandle.readlines()
            l= len(lines)
            self.msg = QMessageBox()
            self.msg.setIcon(QMessageBox.Information)
            self.msg.setWindowIcon(QIcon('ytbico.ico'))
            self.msg.setWindowTitle('Python Youtube Downloader')
            print lines
            if 'youtube.com/' not in str(lines):
                self.msg.setText('Não foram encontrados nenhum link no arquivo {}'.format(str(nome_arquivo)))
                self.msg.exec_()
                self.browse
            else:
                asp = QMessageBox.question(Window(), 'Python Youtube Downloader',  'Foram encontradas {} links no arquivo txt. Continuar ?'.format(str(l)), QMessageBox.Yes, QMessageBox.No)
                if asp == QMessageBox.Yes:
                    asp23 = QMessageBox.question(Window(), 'Python Youtube Downloader', 'Você deseja baixar somente MP3 ?', QMessageBox.Yes, QMessageBox.No)
                    if asp23 == QMessageBox.No:
                        for k in lines:
                            self.iniciar_video('normal', 'True')
                        self.msgt2 =QMessageBox()
                        self.msgt2.setIcon(QMessageBox.Information)
                        self.msgt2.setWindowTitle('Python Youtube Downloader')
                        self.msgt2.setText("{} arquivos MP4 foram baixados, salvos na Área de Trabalho".format(int(l)))
                        self.msgt2.setWindowIcon(QIcon('ytbico.ico'))
                        self.msgt2.exec_()                        
                    else:
                        for k in lines:
                            self.iniciar_audio('normal', 'True')
                        self.msgt2 =QMessageBox()
                        self.msgt2.setIcon(QMessageBox.Information)
                        self.msgt2.setWindowTitle('Python Youtube Downloader')
                        self.msgt2.setText("{} arquivos MP3 foram baixados, salvos na Área de Trabalho".format(int(l)))
                        self.msgt2.setWindowIcon(QIcon('ytbico.ico'))
                        self.msgt2.exec_()
                
            
        
                
app = QApplication(sys.argv)
gui = Window()
sys.exit(app.exec_())
