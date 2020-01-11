# -*- coding: utf-8 -*-

"""
    Programa desarrollado por el Licenciado César Cordero Rodríguez.
    Bajo licencia GPLv3.
    Puede ser modificado, copiado y distribuido.
    Se desarrolló con fines educativos.

"""

import time
import os

def write_file(value, way, file_name):
    os.system("echo " + str(value) + " " + str(way) + " " + str(file_name))

def primes(i, count, total_found):
    write_file(str(i), ">", "primos.last")
    write_file(str(total_found + count), ">", "total_primes.found")

def calculate_primes():
    found = 0
    i = 0

    try:
        number = open("number_of_primes.to_find", "r")
        top = int(number.read())
        number.close()
    except:
        top = 100
        write_file(str(top), ">", "number_of_primes.to_find")

    try:
        total_found_file = open("total_primes.found", "r")
        total_found = int(total_found_file.read())
        total_found_file.close()
    except:
        total_found = 0

    try:
        last = open("primos.last", "r")
        last_n = int(last.read())
        last.close()
    except:
        last_n = 1

    i = last_n

    if total_found > 0:
        count = -1
    else:
        count = 0

    while True:
        if i == 1:
            count+=1
            print("Prime found = " + str(i))
            write_file(str(i), ">>", "primos.list")
            primes(i, count, total_found)
            i+=1
            continue

        found = 2
        for j in range(2, i):
            if i%j == 0:
                found+=1
                break
        if found == 2:
            count+=1
            print("Prime found = " + str(i))
            write_file(str(i), ">>", "primos.list")
            primes(i, count, total_found)

        if count == top:
            primes(i, count, total_found)
            break

        i+=1

    print("Total primes " + str(total_found + count))

inicio = time.time()

calculate_primes()

final = time.time()

print("Final " + str((final - inicio)))

print("Primes Python")
