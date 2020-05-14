# -*- coding: utf-8 -*-

"""
    Programa desarrollado por el Licenciado César Cordero Rodríguez.
    Bajo licencia GPLv3.
    Puede ser modificado, copiado y distribuido.
    Se desarrolló con fines educativos.
"""

X=int(input("Enter value: "))

print("")
print("For X="+str(X))
print("And Y from 0 to 9")
#Another formula to multiply
#print("Formula:")
#print("X*Y=10*Y-((10-X)*Y)")
print("")

Y=0
while(Y<10):
    #Another formula to multiply
    #R=10*Y-((10-X)*Y)
    R=X*Y
    print(str(X) + "*" + str(Y) + "=" + str(R))
    Y+=1
