# coding: utf-8

import sys
import os
import subprocess
import threading
import time
from ytconsole import *

#Variaveis para esconder o conteudo de saida dos comandos de download -> iniciar_video() iniciar_audio()
#Comandos de conversao mostram a saida em uma tela cmd
#Hide output console while downloading
si = subprocess.STARTUPINFO()
si.dwFlags |= subprocess.STARTF_USESHOWWINDOW
CREATE_NO_WINDOW = 0x08000000
#Faca a checkagem de arquivos antes de prosseguir...
#Check files before continue...
os.system('python depends.py')

from PyQt4.QtCore import *
from PyQt4.QtGui import *

x = 1
  
class Window(QMainWindow):
        def __init__(self):
            super(Window, self).__init__()
            self.setGeometry(50,50,700,500)
            self.setWindowTitle('Python Youtube Downloader')
            self.setWindowIcon(QIcon('ytbico.ico'))
            # Barra de menu
            # Menu bar
            extractAction = QAction("Sobre", self)
            extractAction.setShortcut("Ctrl+Q")
            extractAction.setStatusTip('Ler varios objetos a partir de um arquivo de texto')
            extractAction.triggered.connect(self.about)
            mainMenu = self.menuBar()
            fileMenu = mainMenu.addMenu('Ajuda')
            fileMenu.addAction(extractAction)
            self.home()
        def home(self):
            # Imagem principal
            self.pic = QLabel(self)
            self.pic.setPixmap(QPixmap('ytbico.ico'))
            self.pic.setGeometry(234,-120,480,480)
            # Botoes
            self.button5 = QPushButton('Selecionar arquivo...', self)
            self.button5.clicked.connect(self.browse_convert)
            self.button5.resize(121,30)
            self.button5.move(30,420)
            self.button6 = QPushButton('Iniciar', self)
            self.button6.clicked.connect(self.start_convert)
            self.button6.resize(60,40)
            self.button6.move(600,420)
            self.button7 = QPushButton('Abrir lista...', self)
            self.button7.clicked.connect(self.browse)
            self.button7.resize(67,24)
            self.button7.move(520,241)
            self.button8 = QPushButton('Iniciar\nDownload', self)
            self.button8.clicked.connect(self.main)
            self.button8.resize(80,60)
            self.button8.move(420,315)            
            # Entrada de texto para entrada da variavel link
            self.textbox = QLineEdit(self)
            self.textbox.move(230, 242)
            self.textbox.resize(280,22)
            # Caixinhas
            self.cx_video = QCheckBox('Somente video', self)
            self.cx_video.setGeometry(QRect(260,280, 100, 21))   
            self.cx_audio = QCheckBox('Somente audio', self)
            self.cx_audio.setGeometry(QRect(380, 280, 100, 21))            
            self.e = QCheckBox('E:/ (padrao)', self)
            self.e.setGeometry(QRect(290,315, 100, 21))
            self.d = QCheckBox('D:/', self)
            self.d.setGeometry(QRect(290 ,335, 100, 21))
            self.f = QCheckBox('F:/', self)
            self.f.setGeometry(QRect(290,355, 100, 21))            
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
            # Textos do app
            self.sendto = QLabel("Enviar para:", self)
            self.sendto.move(200,323)
            self.sendto.setFont(QFont('Monospace', 10))
            self.tx= QLabel("Insira a URL ->", self)
            self.tx.move(130,237)
            self.tx.setFont(QFont('Monospace', 10))
            self.tx2 = QLabel("Converter para: ", self)
            self.tx2.move(200,420)
            self.line1 = QLabel('  ___________________________________Conversor de Ext.___________________________________ ', self)
            self.line1.move(0, 375)
            self.line1.resize(1000, 20)
            self.line1.setFont(QFont('Verdana', 10))
            self.progress = QProgressBar(self)
            self.progress.setGeometry(11.9, 479, 713, 10)
            #LOCK SIZE ( Nao aumentar o tamanho da janela )
            self.setFixedSize(self.size())
            self.showMaximized()
            #MSG PAINEL
            self.msg = QMessageBox()
            self.msg.setIcon(QMessageBox.Information)
            self.msg.setWindowTitle('Python Youtube Downloader')
            self.msg.setWindowIcon(QIcon('ytbico.ico'))

        def paintEvent(self, e):
            #Retangulo design
            painter = QPainter(self)
            painter.setPen(QPen(Qt.black,2, Qt.SolidLine))
            painter.drawRect(10, 30, 680, 460)
                
        def progress_bar(self): # Barra de progresso inicio
                self.completed = 0
                while self.completed < 45:
                        self.completed += 0.0001
                        self.progress.setValue(self.completed)
        def end_progress_bar(self):
                self.completed = 45 # Barra de progresso fim
                while self.completed < 100:
                        self.completed += 0.0001
                        self.progress.setValue(self.completed)
                
        def slow_progress_bar(self): #Barra de progresso ate o valor 20, por conta de mais arquivos de lista
                self.completed = 0
                while self.completed < 20:
                        self.completed += 0.0001
                        self.progress.setValue(self.completed)
        def end_slow_progress_bar(self): # Final da funcao, para concluir a barra restante
                self.completed = 20
                while self.completed < 60:
                        self.completed += 0.0001
                        self.progress.setValue(self.completed)
                self.completed = 60
                while self.completed < 100:
                        self.completed += 0.0001
                        self.progress.setValue(self.completed)

        def loading_cursor(self):
                #Mouse loading...
                load = QApplication.setOverrideCursor(Qt.WaitCursor)
        def restore_cursor(self):
                #Restore mouse
                restore = QApplication.restoreOverrideCursor()
                

        def start_convert(self):
            #Variavel $tipo serve para identificar o formato final definido pelo usuario
            #String $tipo to know the final format of file
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

            #Abra o arquivo principal
            #Open the source file
            f = file(str(source_arquivo))
            #Descubra o formato do arquivo principal
            f2 = f.name.split('.')
            source_formato = f2[1]
            print 'Arquivo inicial : ' + source_arquivo + '\nFormato inicial ----> ' + source_formato + '\nFormato final ---->' + tipo
            self.msg = QMessageBox()
            self.msg.setIcon(QMessageBox.Information)
            self.msg.setText("A seguir, escolha um nome para seu arquivo.")
            self.msg.setWindowTitle('Python Youtube Downloader')
            self.msg.setWindowIcon(QIcon('ytbico.ico'))
            self.msg.exec_()
            #Escolha o arquivo_final, e o local onde ira ser salvo.
            arquivo_final = QFileDialog.getSaveFileName(self, 'Save File')
            asp = QMessageBox.question(Window(), 'Deseja prosseguir ?',  'Arquivo: {}\nFormato inicial: {}\nFormato final: {}'
                                       .format(str(source_arquivo),str(source_formato), str(tipo)), QMessageBox.Yes, QMessageBox.No)
            if asp == QMessageBox.Yes:
                print tipo
                if tipo == 'avi' or tipo == 'mkv' or tipo == 'wmv' or tipo == 'mov' or tipo =='aac' or tipo == 'flac' or tipo == 'wma' or tipo == 'mp3':
                    
                    """ O codigo '"{}"' faz com que o windows nao bugue na hora de encontrar o
                    arquivo e pasta como nomes
                    separados, ex : C:\Users\Video de luta.mp4 ou C:/Users/Documents/Shared and Shares/video.mp4
                    pois ficaria : ffmpeg -i C:\Users\Documents\Shares and Shares\video.mp4 ocasionando erro por razao dos espacos entre as pastas.
                    
                    source_arquivo_final = Arquivo de origem modificado com adicao de aspas para evitar erro do ffmpeg.exe 
                    arquivo_final = Nome dado pelo usuario ao arquivo que ira ser salvo
                    af = Modificacao da variavel $arquivo_final, acrescentando o .(extensao)
                    final_dos_finais = Por fim, modifica a variavel $af adicionando aspas para evitar o erro do ffmpeg.exe
                    """
                    source_arquivo_final = '"{}"'.format(source_arquivo)
                    af = arquivo_final + '.' + tipo
                    final_dos_finais = '"{}"'.format(af)
                    convert_command = 'ffmpeg -i {} {}'.format(str(source_arquivo_final), str(final_dos_finais))
                    #LOG
                    print '\n1.[*] Arquivo iniciado ----> {}'.format(source_arquivo_final)
                    print '\n2.[*] Analisando extensao de arquivo {}---->{}'.format(af, tipo)
                    print '\n3.[*] Arquivo final ---->{}'.format(final_dos_finais)
                    print '\n4.[*] Iniciando comando : {}'.format(convert_command)
                    #LOG
                    self.loading_cursor()                
                    os.system(convert_command)
                    self.restore_cursor()
                    print '\n5.[*] Finalizado'             
                    self.msg = QMessageBox()
                    self.msg.setIcon(QMessageBox.Information)
                    self.msg.setWindowIcon(QIcon('ytbico.ico'))
                    self.msg.setWindowTitle('Python Youtube Downloader')
                    self.msg.setText("Arquivo final \nsalvo em {}".format(final_dos_finais))
                    self.msg.show()
                                
        def browse_convert(self):
            x += 1
            #self.tx5 variavel de ambiente, mostra a path onde o arquivo foi aberto, ex: "C:/users/usuario/mktp.mp3"
            #Clear the content before repeat ( limpa o conteudo da variavel self.tx5 antes de preencher outra em caso de erro do usuario )
            #Se o numero de repeticoes for igual a 2, entao a variavel e zerada.
            if x >= 3:
                try:
                        self.tx5.clear()
                except:
                        pass
            global source_arquivo
            source_arquivo = QFileDialog.getOpenFileName()
            try:
                    print 'Arquivo selecionado -->' + source_arquivo + '\n'
                    self.tx5 = QLabel("({})".format(source_arquivo), self)
                    #Resize for increase the text ( redimensionar o tamanho para aparecer todo o conteudo do texto )
                    self.tx5.resize(250,20)
                    self.tx5.move(12,455)
                    self.tx5.setFont(QFont('Verdana', 8))
                    self.tx5.show()                    
            except UnicodeEncodeError: #Erro na hora de ler um arquivo de entrada, se houver acentos e caracteres especiais
                    self.msg = QMessageBox()
                    self.msg.setIcon(QMessageBox.Information)
                    self.msg.setWindowIcon(QIcon('ytbico.ico'))
                    self.msg.setWindowTitle('Python Youtube Downloader')
                    self.msg.setText('O arquivo selecionado nao pode conter acentos e \ncaracteres especiais !')
                    self.msg.show()
            
            

        def about(self):
            #Mensagem README
            self.msgt = QMessageBox()
            self.msgt.setIcon(QMessageBox.Information)
            self.msgt.setWindowTitle('Python Youtube Downloader')
            self.msgt.setText("""Aplicativo para download e conversao de conteudo do Youtube.

Dispositivo padrao = E:/

O dispositivo configurado pode ser alterado
na variavel disk_path em ytdown.py

Para ver as bibliotecas necessarias consulte o arquivo README
Link do projeto: https://github.com/richardparker6103/ytdown/blob/master/
""")
            self.msgt.setWindowIcon(QIcon('ytbico.ico'))
            self.msgt.show()
            
        def browse(self, convert=False):
            global k
            global lines
            nome_arquivo = QFileDialog.getOpenFileName()
            print 'filePath' + nome_arquivo + '\n'
            fileHandle = open(nome_arquivo, 'r')
            #Search if this TXT ( Descubra se e TXT )
            if ".txt" in nome_arquivo:
                print "e TXT"
            else:
                print "NAO E TXT\n ALERTANDO..."
                self.msgt = QMessageBox()
                self.msgt.setIcon(QMessageBox.Information)
                self.msgt.setWindowTitle('Python Youtube Downloader')
                self.msgt.setText("O arquivo {} selecionado nao e valido, selecione um arquivo em formato .txt".format(str(nome_arquivo)))
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
            #Search if this file have yt links ( Descubra se o arquivo aberto possui links validos. )
            if 'youtube.com/' not in str(lines):
                self.msg.setText('Nao foram encontrados nenhum link no arquivo {}'.format(str(nome_arquivo)))
                self.msg.exec_()
            else:
                self.msg.setText('Foram encontradas {} links no arquivo\n{}'.format(str(l), str(nome_arquivo)))
                self.msg.exec_()
                self.tx7 = QLabel('{}'.format(nome_arquivo), self)
                self.tx7.resize(250,20)
                self.tx7.move(490,270)
                self.tx7.setFont(QFont('Monospace', 9))
                self.tx7.show()
                self.list_active = True
        def start_all(self, link, ft, disk_path, list_active):
            # ft is format = mp3, mp4
            #If disk_path is True
                if disk_path:
                        try:
                                #Tenta entrar no diretorio do dispositivo, caso haja algum error e porque ele nao foi conectado.
                                s = os.chdir(disk_path)
                                print "[*] Dispositivo encontrado -> {}".format(disk_path)
                                print "[*] Alterando diretorio para -> {}".format(script_dir)
                                s = os.chdir(script_dir)
                                if self.list_active:
                                        if ft == '.mp4':
                                                self.slow_progress_bar()
                                                self.loading_cursor()                                        
                                                for k in lines:
                                                        cmd = os.system('python ytconsole.py -v -d "{}" -l "{}"'.format(disk_path, k))
                                                self.end_slow_progress_bar()
                                                self.restore_cursor()
                                                self.msg.setText("{} Arquivos baixados\ntodos enviados para {}".format(len(lines), disk_path))
                                                self.msg.exec_()                                                          
                                        else:
                                                self.slow_progress_bar()
                                                self.loading_cursor()
                                                for k in lines:
                                                        cmd = os.system('python ytconsole.py -a -d "{}" -l {}'.format(disk_path, k))
                                                self.end_slow_progress_bar()
                                                self.restore_cursor()
                                                self.msg.setText("{} arquivos baixados\ntodos enviados para {}".format(len(lines), disk_path))
                                                self.msg.exec_()
                                else:
                                        if ft == '.mp4':
                                                self.progress_bar()
                                                self.loading_cursor()                                        
                                                cmd = os.system('python ytconsole.py -v -d "%s" -l "%s"'%(disk_path, link))
                                                print "[*] O comando foi terminado"
                                                print "[*] Resultado -> {}".format(cmd)
                                                self.end_progress_bar()
                                                self.restore_cursor()                                        
                                                self.msg.setText("Finalizado\narquivos enviados para {}".format(disk_path))
                                                #continue
                                                self.msg.exec_()
                                        else:
                                                self.progress_bar()
                                                self.loading_cursor()
                                                cmd = os.system('python ytconsole.py -a -d "%s" -l "%s"'%(disk_path, link))
                                                self.end_progress_bar()
                                                self.restore_cursor()                                        
                                                self.msg.setText("Finalizado\narquivos enviados para {}")
                                                self.msg.exec_()
                        except WindowsError:
                                self.msg.setText('Dispositivo {} desconectado, conecte e tente novamente.'.format(disk_path))
                                self.msg.exec_()
                else:
                        if self.list_active:
                                if ft == '.mp4':
                                        self.slow_progress_bar()
                                        self.loading_cursor()                                        
                                        for k in lines:
                                                cmd = os.system('python ytconsole.py -v -l %s' %k)
                                        self.end_slow_progress_bar()
                                        self.restore_cursor()                                        
                                        self.msg.setText("{} arquivos baixados.".format(len(lines)))
                                        self.msg.exec_()                                                             
                                else:
                                        self.slow_progress_bar()
                                        self.loading_cursor()
                                        for k in lines:
                                                cmd =os.system('python ytconsole.py -a -l %s' %k)
                                        self.end_slow_progress_bar()
                                        self.restore_cursor()
                                        self.msg.setText("{} Arquivos baixados.".format(len(lines)))
                                        self.msg.exec_()
                        else:
                                if ft == '.mp4':
                                        self.slow_progress_bar()
                                        self.loading_cursor()                                        
                                        cmd = os.system('python ytconsole.py -v -l %s' %link)
                                        self.end_slow_progress_bar()
                                        self.restore_cursor()                                        
                                        self.msg.setText("  Finalizado.")
                                        self.msg.exec_()                                                             
                                else:
                                        self.progress_bar()
                                        self.loading_cursor()
                                        cmd = os.system('python ytconsole.py -a -l %s' %link)
                                        self.end_progress_bar()
                                        self.restore_cursor()
                                        self.msg.setText("  Finalizado")
                                        self.msg.exec_()  
                                           
        def main(self):
                global disk_path
                link = self.textbox.text()
                if self.e.isChecked():
                        disk_path = 'E:/'
                elif self.d.isChecked():
                        disk_path = 'D:/'
                elif self.f.isChecked():
                        disk_path = 'F:/'
                else:
                        disk_path = False
                        
                if self.cx_video.isChecked():
                        ft = '.mp4'
                elif self.cx_audio.isChecked():
                        ft = '.mp3'
                else:
                        self.msg.setText('Selecione uma opcao para video/audio !')
                        self.msg.exec_()
                         
                try:      
                        self.start_all(link, ft, disk_path, self.list_active)
                except: #Exception for list  False ( Excecao para o caso de nao haver listas )
                        print "[*] Arquivo de lista e falso, ignorando ..."
                        self.list_active = False
                        self.start_all(link, ft, disk_path, self.list_active)
                
                
                
                                
                        
                        
app = QApplication(sys.argv)
gui = Window()
sys.exit(app.exec_())
