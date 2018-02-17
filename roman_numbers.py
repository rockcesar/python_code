# -*- coding: utf-8 -*-

"""

    Programa desarrollado por el Licenciado César Cordero Rodríguez.
    Bajo licencia GPLv3.
    Puede ser modificado, copiado y distribuido.
    Se desarrolló con fines educativos.

"""

#
# Running example:
# python roman_numbers.py MMXVIII
# Result: The decimal number is 2018
#
# python roman_numbers.py MMXXX
# Result: The decimal number is 2030
#

import sys

roman_number={'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

def repetitive_number(string, count, qty):
    repetitive_counter = 0
    if count+qty < len(string):
        while repetitive_counter < qty+1:
            if string[count + repetitive_counter] == string[count]:
                repetitive_counter+=1
            else:
                break
    if repetitive_counter == qty+1:
        return None
    else:
        return True

def roman_numeral_to_int(string):

    count = 0
    total = 0
    
    if type(string) is not str:
        return None
    
    if not string:
        return None
    
    while count < len(string):
        if string[count] not in roman_number:
            return None
        elif string[count] == 'I':
            if count+1 < len(string) and string[count+1] == 'X':
                total += roman_number['X'] - roman_number['I']
                count += 1
            elif count+1 < len(string) and string[count+1] == 'V':
                total += roman_number['V'] - roman_number['I']
                count += 1
                if count+1 < len(string):
                    return None
            elif count+1 < len(string) and string[count+1] in ['M', 'D', 'C', 'L']:
                return None
            else:
                total += roman_number['I']
                if not repetitive_number(string, count, 3):
                    return None
        elif string[count] == 'V':
            total += roman_number[string[count]]
            if count+1 < len(string) and string[count+1] in ['M', 'D', 'C', 'L', 'X']:
                return None
            if not repetitive_number(string, count, 1):
                return None
        elif string[count] == 'X':
            if count+1 < len(string) and string[count+1] == 'L':
                total += roman_number['L'] - roman_number['X']
                count += 1
            elif count+1 < len(string) and string[count+1] == 'C':
                total += roman_number['C'] - roman_number['X']
                count += 1
            elif count+1 < len(string) and string[count+1] in ['M', 'D']:
                return None
            else:
                total += roman_number['X']
                if not repetitive_number(string, count, 3):
                    return None
        elif string[count] == 'L':
            total += roman_number[string[count]]
            if count+1 < len(string) and string[count+1] in ['M', 'D', 'C']:
                return None
            if not repetitive_number(string, count, 1):
                return None
        elif string[count] == 'C':
            if count+1 < len(string) and string[count+1] == 'D':
                total += roman_number['D'] - roman_number['C']
                count += 1
            elif count+1 < len(string) and string[count+1] == 'M':
                total += roman_number['M'] - roman_number['C']
                count += 1
            elif count+1 < len(string) and string[count+1] in ['M']:
                return None
            else:
                total += roman_number['C']
                if not repetitive_number(string, count, 3):
                    return None
        elif string[count] == 'D':
            total += roman_number[string[count]]
            if count+1 < len(string) and string[count+1] in ['M']:
                return None
            if not repetitive_number(string, count, 1):
                return None
        elif string[count] == 'M':
            total += roman_number[string[count]]

        count += 1

    return total

#roman_n = raw_input("Enter the roman number: ")
roman_n = sys.argv[1]

print("The decimal number is " + str(roman_numeral_to_int(roman_n)))
