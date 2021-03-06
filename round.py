# -*- coding: utf-8 -*-

"""

    Programa desarrollado por el Licenciado César Cordero Rodríguez.
    Bajo licencia GPLv3.
    Puede ser modificado, copiado y distribuido.
    Se desarrolló con fines educativos.

"""

#
# It does the function of 
# MULTIPLO.SUPERIOR.XCL in Excel in Microsoft Office 
#                       and Calc in LibreOffice
#
# Running example:
# python round.py 5.9 0.9 2
# Result: Rounded 6.3
#
# python round.py 5.9 0.3442 4
# Result: Rounded 6.1956
#

import sys

def _get_multiple_up_rounded(number, rounded, number_of_decimals):
    result_mod = round(float(number%rounded), int(number_of_decimals))
    if result_mod != 0:
        
        result = round(float((number - result_mod) + rounded), int(number_of_decimals))
    else:
        result = round(float(number), int(number_of_decimals))
    return result

number_of_decimals = sys.argv[3]
number = round(float(sys.argv[1]), int(number_of_decimals))
rounded = float(sys.argv[2])

print("Rounded " + str(_get_multiple_up_rounded(number, rounded, number_of_decimals)))
