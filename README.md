- Aplicativo para download e conversão de conteudo do Youtube.
Bibliotecas necessarias:

youtube_dl
clint
bs4
progress

Todas elas estao no arquivo requirements.txt, para instalar elas digite: pip install -r requirements.txt




A variavel disk_path pode ser alterada em ytdown.py para quaisquer dispositivo ( E:/, D:/, C:/ )

[CONSOLE] 

Baixar somente video: 

python2.7 ytconsole.py --video --link _LINK_ 
python2.7 ytconsole.py --video -p --link _LINK_ ( p=Send to disk_path )

Baixar e extrair audio:

python2.7 ytconsole.py --audio --link _LINK_
python2.7 ytconsole.py --audio -p --link _LINK_ ( p= Send to disk_path )





