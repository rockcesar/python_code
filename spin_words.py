# -*- coding: utf-8 -*-

"""

    Programa desarrollado por el Licenciado César Cordero Rodríguez.
    Bajo licencia GPLv3.
    Puede ser modificado, copiado y distribuido.
    Se desarrolló con fines educativos.

"""

# Words with more than 4 letters, should be spinned, in a sentence
# IN: Hi and Welcome
# OUT: Hi and emocleW

def spin_words(sentence):
    list_words = sentence.split(' ')
    return ' '.join([l[::-1] if len(l) >= 5 else l for l in list_words])
