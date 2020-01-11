# -*- coding: utf-8 -*-

"""
    Programa desarrollado por el Licenciado César Cordero Rodríguez.
    Bajo licencia GPLv3.
    Puede ser modificado, copiado y distribuido.
    Se desarrolló con fines educativos.

"""

# A translator in Python using Tor Proxy:

from py_translator import Translator
import sys

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
   file = open(sys.argv[1], "r")
   text = file.read()

s = Translator(proxies=proxy).translate(text=text, dest=sys.argv[2]).text

print(s)
