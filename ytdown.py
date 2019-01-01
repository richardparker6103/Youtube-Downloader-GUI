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
                extractAction = QAction("Sobre", self)
                extractAction.setShortcut("Ctrl+Q")
                extractAction.setStatusTip('Ler varios objetos a partir de um arquivo de texto')
                extractAction.triggered.connect(self.about)
                mainMenu = self.menuBar()
                fileMenu = mainMenu.addMenu('Arquivo')
                fileMenu.addAction(extractAction)
                self.home()
        def home(self):
            global tipo
            self.pic = QLabel(self)
            self.pic.setPixmap(QPixmap('ytbico.ico'))
            self.pic.setGeometry(234,-120,480,480)
            self.button = QPushButton('Somente vídeo', self)
            self.button.clicked.connect(self.iniciar_video)
            self.button.resize(100,30)
            self.button.move(260,280)
            self.button2 = QPushButton('Somente áudio', self)
            self.button2.clicked.connect(self.iniciar_audio)
            self.button2.move(380,280)
            self.button2.resize(100, 30)
            self.button4 = QPushButton('Baixar em \ndispositivo', self)
            self.button4.clicked.connect(self.iniciar_audio_pendrive)
            self.button4.resize(80,35)
            self.button4.move(315,330)
            self.button5 = QPushButton('Selecionar arquivo...', self)
            self.button5.clicked.connect(self.browse_convert)
            self.button5.resize(121,30)
            self.button5.move(30,420)
            self.button6 = QPushButton('Iniciar', self)
            self.button6.clicked.connect(self.iniciar_conversao)
            self.button6.resize(60,40)
            self.button6.move(600,420)
            self.button7 = QPushButton('Abrir lista...', self)
            self.button7.clicked.connect(self.browse)
            self.button7.resize(75,26)
            self.button7.move(520,238)
            self.textbox = QLineEdit(self)
            self.textbox.move(230, 240)
            self.textbox.resize(270,25)
            self.e = QCheckBox('E:/ (padrão)', self)
            self.e.setGeometry(QRect(440,320, 100, 21))
            self.d = QCheckBox('D:/', self)
            self.d.setGeometry(QRect(440,340, 100, 21))
            self.f = QCheckBox('F:/', self)
            self.f.setGeometry(QRect(440,360, 100, 21))            
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
            self.mp3 = QCheckBox('MP3', self)
            self.mp3.setGeometry(QRect(300, 460, 71,21))
            self.flac = QCheckBox('FLAC', self)
            self.flac.setGeometry(QRect(300, 440, 71,21))
            self.tx = QLabel("Insira a URL ->", self)
            self.tx.move(110,235)
            self.tx.setFont(QFont('Monospace', 11))
            self.tx2 = QLabel("Converter para: ", self)
            self.tx2.move(200,420)
            self.linha2 = QLabel('  ___________________________________Conversor de Ext.___________________________________ ', self)
            self.linha2.move(0, 375)
            self.linha2.resize(1000, 20)
            self.linha2.setFont(QFont('Verdana', 10))
            self.seta1 = QLabel('-->', self)
            self.seta1.move(410, 333)
            self.seta1.resize(20,20)
            self.seta1.setFont(QFont('Monospace', 10))
            painter = QPainter(self)
            painter.setPen(QPen(Qt.black, 10, Qt.SolidLine))
            painter.drawRect(100, 15, 400, 200)
            #LOCK SIZE ( Não aumentar o tamanho da janela )
            self.setFixedSize(self.size())
            
            self.showMaximized()

        def paintEvent(self, e):
            painter = QPainter(self)
            painter.setPen(QPen(Qt.black,2, Qt.SolidLine))
            painter.drawRect(10, 30, 680, 460)
        
        def iniciar_video(self, estado='normal', lista='False'):
            try:
                global link
                #Mouse wait ()
                QApplication.setOverrideCursor(Qt.WaitCursor)
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
                        subprocess.call('python os2.py -v -l %s' %link, creationflags=CREATE_NO_WINDOW)
                        if lista == 'False':
                            self.msg = QMessageBox()
                            self.msg.setIcon(QMessageBox.Information)
                            self.msg.setText("Vídeo salvo na área de trabalho")
                            self.msg.setWindowTitle('Python Youtube Downloader')
                            self.msg.setWindowIcon(QIcon('ytbico.ico'))
                            self.msg.exec_()                                  
                        else:
                            pass
            finally:
                #Restore the current mouse
                QApplication.restoreOverrideCursor()
                     
        def iniciar_audio_pendrive(self):
                global disk_path
                if self.d.isChecked():
                    disk_path = 'D:/'
                elif self.f.isChecked():
                    disk_path = 'F:/'
                else:
                    disk_path = 'E:/'
                link = self.textbox.text()
                try:
                    s = os.chdir(disk_path)
                    os.chdir(local_path)
                    subprocess.call('python os2.py -a -p -l %s' %link, creationflags=CREATE_NO_WINDOW)
                    self.msg = QMessageBox()
                    self.msg.setIcon(QMessageBox.Information)
                    self.msg.setWindowTitle('Python Youtube Downloader')
                    self.msg.setText("O arquivo MP3 foi salvo no pendrive %s" %disk_path)
                    self.msg.setWindowIcon(QIcon('ytbico.ico'))
                    self.msg.exec_()                     
                except WindowsError:
                    global x
                    x = x + 1
                    self.msg2 = QMessageBox()
                    self.msg2.setIcon(QMessageBox.Information)
                    self.msg2.setWindowTitle('Python Youtube Downloader')
                    self.msg2.setText('Dispositivo {} desconectado, conecte e tente novamente.'.format(disk_path))
                    self.msg2.setWindowIcon(QIcon('ytbico.ico'))
                    self.msg2.exec_()
                    
                

                
        def iniciar_audio(self, estado='normal', lista='False'):
            try:
                QApplication.setOverrideCursor(Qt.WaitCursor)
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
                        subprocess.call('python os2.py -a -l %s' %link, creationflags=CREATE_NO_WINDOW)
                        if lista == 'False':
                            self.msg = QMessageBox()
                            self.msg.setIcon(QMessageBox.Information)
                            self.msg.setText("Vídeo salvo na área de trabalho")
                            self.msg.setWindowTitle('Python Youtube Downloader')
                            self.msg.setWindowIcon(QIcon('ytbico.ico'))
                            self.msg.exec_()                                  
                        else:
                            pass
            finally:
                QApplication.setOverrideCursor(Qt.WaitCursor)

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
            elif self.mp3.isChecked():
                tipo = 'mp3'                
                    
            f = file(str(source_arquivo))
            f2 = f.name.split('.')
            source_formato = f2[1]
            print 'Arquivo inicial : ' + source_arquivo + '\nFormato inicial ----> ' + source_formato + '\nFormato final ---->' + tipo
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
                if tipo == 'avi' or tipo == 'mkv' or tipo == 'wmv' or tipo == 'mov' or tipo =='aac' or tipo == 'flac' or tipo == 'wma' or tipo == 'mp3':
                    
                    """ The '"{}"' bypass windows error by space ( O código '"{}"' faz com que o windows não bugue
                    na hora de encontrar o
                    arquivo e pasta como nomes
                    separados, ex : "C:\Users\Video de luta.mp4
                    """
                    source_arquivo_final = '"{}"'.format(source_arquivo)
                    af = arquivo_final + '.' + tipo
                    final_dos_finais = '"{}"'.format(af)
                    convert_command = 'ffmpeg -i {} {}'.format(str(source_arquivo_final), str(final_dos_finais))
                    #LOG
                    print '1.[*] Arquivo iniciado ----> {}'.format(source_arquivo_final)
                    print '\n2.[*] Analisando extensão de arquivo {}---->{}'.format(af, tipo)
                    print '\n3.[*] Arquivo final ---->{}'.format(final_dos_finais)
                    print '\n4.[*] Iniciando comando : {}'.format(convert_command)
                    #LOG
                    os.system(convert_command)
                    print '\n5.[*] Finalizado'             
                    self.msg = QMessageBox()
                    self.msg.setIcon(QMessageBox.Information)
                    self.msg.setWindowIcon(QIcon('ytbico.ico'))
                    self.msg.setWindowTitle('Python Youtube Downloader')
                    self.msg.setText("Arquivo final \nsalvo em {}".format(final_dos_finais))
                    self.msg.show()
                    
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
            source_arquivo = QFileDialog.getOpenFileName()
            print 'Arquivo selecionado -->' + source_arquivo + '\n'
            self.tx5 = QLabel("({})".format(source_arquivo), self)
            #Resize for increase the text ( redimensionar o tamanho para aparecer todo o conteúdo do texto )
            self.tx5.resize(250,20)
            self.tx5.move(2,455)
            self.tx5.setFont(QFont('Verdana', 8))
            self.tx5.show()
            
            

        def about(self):
            self.msgt = QMessageBox()
            self.msgt.setIcon(QMessageBox.Information)
            self.msgt.setWindowTitle('Python Youtube Downloader')
            self.msgt.setText("""YtDown aplicativo para download e conversão de conteúdo do Youtube.

Dispositivo padrão = E:/

O dispositivo configurado pode ser alterado
na varíavel disk_path em ytdown.py

Para ver as bibliotecas necessárias consulte o arquivo README
Link do projeto: https://github.com/richardparker6103/ytdown/blob/master/
""")
            self.msgt.setWindowIcon(QIcon('ytbico.ico'))
            self.msgt.show()           
        def browse(self, convert=False):
            global k
            nome_arquivo = QFileDialog.getOpenFileName()
            print 'filePath' + nome_arquivo + '\n'
            fileHandle = open(nome_arquivo, 'r')
            #Search if this TXT ( Descubra se é TXT )
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
            #Search if this file have yt links ( Descubra se o arquivo aberto possui links válidos. )
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
