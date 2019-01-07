# -*- coding: cp1252 -*-

import os
import time

def disable_apps():
        time.sleep(1.2)
        print "----------------Limpeza de apps inuteis----------------"
        time.sleep(3)
        print "\n[*] Serao apagados os seguintes aplicativos do sistema: \n"
	print "3dbuilder\nwindowsalarms\nwindowscalculator\nwindowscommunicationsapps\nwindowscamera"
	print "officehub\nskypeapp\nzunemusic\nwindowsmaps\nsolitairecollection\nbingfinance\nzunevideo"
	print "bingnews\nnonenote\npeople\nwindowsphone\nphotos\nwindowsstore\nbingsports\nsoundrecorder"
	print "bingweather\nxboxapp\n"
	askk = raw_input('Deseja continuar ? : [S/n]')
	if askk == 'n':
                exit()
        else:
                for x in range(22):
                        os.system("Get-AppxPackage *3dbuilder* | Remove-AppxPackage"   
                
                
	
def disco():
	print "----------------Correcao de uso 100% disco-----------------"
	time.sleep(2)
	time.sleep(4)
	asp = raw_input("\n[*] O processo pode demorar alguns minutos, deseja continuar ? [S/n]")
	if str(asp) == 'n':
		exit()
	else:
		print "\[*]Iniciando..."
		time.sleep(1.5)
		os.system('Dism /Online /Cleanup-Image /ScanHealth')
		print "[*] Checkagem concluida, partindo para proxima..."
		time.sleep(4)
		os.system('Dism /Online /Cleanup-Image /RestoreHealth')
		print "\n[*] Verificação concluída, reinicie seu PC e confira se está tudo OK"
		time.sleep(3)
		exit()

def main():
        if __name__ == "__main__":
                ask = raw_input('---------------------------------------\n[1] Limpeza de apps inuteis do Windows\n[2] Correcao bug de disco 100%\n\n[*] Escolha: ')
                if ask == '1':
                        disable_apps()
                elif ask == '2':
                        disco()
                else:
                        print "\n[*] Escolha uma opcao valida !"
                        time.sleep(2.7)
                        main()
                        
main()              
        
