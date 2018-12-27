# -*- coding: cp1252 -*-
#------------------README-------------------------
#Necessário executáveis ffmpeg, ffprobe, ffplay !
#Por falta de espaço do github, é necessário baixar manualmente os componentes no site:
#FFMPEG -> (ffmpeg, ffplay, ffprobe) https://www.ffmpeg.org/download.html
#LIBAV -> (para evitar conflitos com o ffmpeg)
#youtube-dl.exe(para download e conversão dos arquivos) -> https://youtube-dl.org/
#PyQt biblioteca para edição GUI -> https://sourceforge.net/projects/pyqt/files/PyQt4/
#------------------README-------------------------
# Required executable ffmpeg, ffprobe, ffplay!
#For lack of space of github, is to download the media components on the site:
#FFMPEG -> (ffmpeg, ffplay, ffprobe) https://www.ffmpeg.org/download.html
#LIBAV -> (to avoid with ffmpeg)
# youtube-dl.exe (for download and file conversion) -> https://youtube-dl.org/
#PyQt library for GUI editing -> https://sourceforge.net/projects/pyqt/files/PyQt4/
#------------------README-------------------------

import sys
import os
from os2 import *
from PyQt4.QtCore import *
from PyQt4.QtGui import *
import time

example = 'https://www.youtube.com/watch?v=C0DPdy98e4c'
x = 1
local_path = os.getcwd()

class Window(QMainWindow):
        def __init__(self):
                super(Window, self).__init__()
                self.setGeometry(50,50,500,300)
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
                self.pic = QLabel(self)
                self.pic.setPixmap(QPixmap('ytb2.ico'))
                self.pic.move(138,0)
                self.pic.resize(300,145)
                self.button = QPushButton('Baixar Vídeo', self)
                self.button.clicked.connect(self.iniciar_video)
                self.button.resize(100,30)
                self.button.move(210,210)
                self.button2 = QPushButton('Baixar MP3', self)
                self.button2.clicked.connect(self.iniciar_audio)
                self.button2.move(210, 170)
                self.button3 = QPushButton('Baixar MP3 direto em pendrive', self)
                self.button3.clicked.connect(self.iniciar_audio_pendrive)
                self.button3.resize(160,30)
                self.button3.move(180,250)
                self.textbox = QLineEdit(self)
                self.textbox.move(130, 145)
                self.textbox.resize(270,23)
                self.progress = QProgressBar(self)
                self.progress.setGeometry(0, 280, 550, 20)
                self.tx = QLabel("LINK: ", self)
                self.tx.move(90,140)
                self.show()
                
        def iniciar_video(self, estado='normal', lista='False'):
                if lista == 'True':
                    link = k
                else:
                    link = self.textbox.text()
                    if link < 40:
                        self.msg = QMessageBox()
                        self.msg.setIcon(QMessageBox.Information)
                        self.msg.setText("Link invalido, por favor, digite um link valido.")
                        self.msg.setWindowTitle('Python Youtube Downloader')

                self.completed = 0
                comando1 = os.system('python os2.py -v -l %s > NUL'%link)
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
                except WindowsError:
                    global x
                    x = x + 1
                    self.msg2 = QMessageBox()
                    self.msg2.setIcon(QMessageBox.Information)
                    self.msg2.setWindowTitle('Python Youtube Downloader')
                    self.msg2.setText('Pendrive desconectado, conecte e aperte em OK')
                    self.msg2.exec_()
                    self.iniciar_audio_pendrive()
                
                os.chdir(local_path)
                comando4 = os.system('python os2.py -a -p -l %s > NUL' %link)
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
                
        def iniciar_audio(self, estado='normal', lista='False'):
                if lista == 'True':
                    link = k
                else:
                    link = self.textbox.text()
                if link < 40:
                    self.msg = QMessageBox()
                    self.msg.setIcon(QMessageBox.Information)
                    self.msg.setText("Link invalido, por favor, digite um link valido.")
                    self.msg.setWindowTitle('Python Youtube Downloader')
                    self.msg.setWindowIcon(QIcon('ytbico.ico'))
                if estado == 'pnd':
                        comando2 = os.system('python os2.py -a -p -l %s > NUL' %link)
                else:
                        comando2 = os.system('python os2.py -a -l %s > NUL' %link)
                if lista == 'False':
                    while self.completed < 100:
                        self.completed += 0.0001
                        self.progress.setValue(self.completed)
                    self.msg = QMessageBox()
                    self.msg.setIcon(QMessageBox.Information)
                    self.msg.setText("MP3 salvo na área de trabalho")
                    self.msg.setWindowTitle('Python Youtube Downloader')
                    self.msg.setWindowIcon(QIcon('ytbico.ico'))
                    self.msg.exec_()                                  
                else:
                    pass




        def browse(self):
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
                if asp == QMessageBox.No:
                    exit()
                else:
                    asp23 = QMessageBox.question(Window(), 'Python Youtube Downloader', 'Você deseja baixar somente MP3 ?', QMessageBox.Yes, QMessageBox.No)
                    if asp23 == QMessageBox.No:
                        for k in lines:
                            self.iniciar_video('normal', 'True')
                    else:
                        for k in lines:
                            self.iniciar_audio('normal', 'True')
                    self.msgt2 =QMessageBox()
                    self.msgt2.setIcon(QMessageBox.Information)
                    self.msgt2.setWindowTitle('Python Youtube Downloader')
                    self.msgt2.setText("{} arquivos foram baixados, salvos na Área de Trabalho".format(int(l)))
                    self.msgt2.setWindowIcon(QIcon('ytbico.ico'))
                    self.msgt2.exec_()
                
            
        
                
app = QApplication(sys.argv)
gui = Window()
sys.exit(app.exec_())
