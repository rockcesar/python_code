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

proxy = {
        'socks': 'socks://localhost:9050',
        'socks': 'socks://localhost:9050',
}
s = Translator(proxies=proxy).translate(text=sys.argv[1], dest='es').text
print(s)
