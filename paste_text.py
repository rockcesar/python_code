"""

    Programa desarrollado por el Licenciado César Cordero Rodríguez.
    Bajo licencia GPLv3.
    Puede ser modificado, copiado y distribuido.
    Se desarrolló con fines educativos.

    Paste Text after 2 seconds.

"""

from pynput.keyboard import Key, Controller
import time

keyboard = Controller()

password="text_pasted"

time.sleep(2)

for s in password:
    keyboard.press(s)
    keyboard.release(s)
