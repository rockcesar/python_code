# -*- coding: utf-8 -*-

"""
    Programa desarrollado por el Licenciado César Cordero Rodríguez.
    Bajo licencia GPLv3.
    Puede ser modificado, copiado y distribuido.
    Se desarrolló con fines educativos.
    
    Si se hacen copias, debe ser referido el autor: Licenciado César Cordero Rodríguez.
"""

# A translator in Python using Tor Proxy:

from py_translator import Translator
import sys

#from py_translator import TEXTLIB

proxy = {
        'socks': 'socks://localhost:9050',
        'socks': 'socks://localhost:9050',
}

ROTATING_PROXY_LIST = {
    'socks': 'socks://localhost:9050'
}

text = ""

if len(sys.argv) == 3:
   text = sys.argv[1]
elif len(sys.argv) == 4 and sys.argv[3] == "using_file":
   file = open("file_to_translate.txt", "r")
   text = file.read()

s = Translator(proxies=proxy).translate(text=text, dest=sys.argv[2]).text

print(s)
