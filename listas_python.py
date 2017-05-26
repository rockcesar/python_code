# -*- coding: utf-8 -*-

"""

    Programa desarrollado por el Licenciado César Cordero Rodríguez.
    Bajo licencia GPLv3.
    Puede ser modificado, copiado y distribuido.
    Se desarrolló con fines educativos.

"""

class nodo():
    valor = None
    sig = None
    atras = None
    der = None
    
    def __init__(self, valor):
        self.valor = valor
        sig = None
        atras = None
        der = None
    
    def setAdelante(self, sig):
        self.sig = sig
    
    def setAtras(self, atras):
        self.atras = atras
    
    def setDerecha(self, der):
        self.der = der

class lista():
    primero = None
    ultimo = None
    
    def __init__(self):
        self.ultimo = self.primero = None
        
    def addNodo(self, valor):
        if self.primero == None:
            self.primero = self.ultimo = nodo(valor)
        else:
            self.ultimo.sig = nodo(valor)
            self.ultimo = self.ultimo.sig
            
    def delNodo(self, valor):
        borrado = False
        temp = self.primero
        if temp != None and temp.valor == valor:
            if self.primero != ultimo:
                self.primero = self.primero.sig
                temp = None
                borrado = True
        if borrado == False:
            while temp.sig != None and borrado == False:
                if temp.sig.valor == valor:
                   temp.sig = temp.sig.sig
                   borrado = True
                temp = temp.sig
    
    def recorrerLista(self):
        temp = self.primero
        while temp != None:
            print str(temp.valor)
            temp = temp.sig

class listaDoble():
    primero = None
    ultimo = None
    
    def __init__(self):
        self.ultimo = self.primero = None
        
    def addNodo(self, valor):
        if self.primero == None:
            self.primero = self.ultimo = nodo(valor)
        else:
            self.ultimo.sig = nodo(valor)
            self.ultimo.sig.atras = self.ultimo
            self.ultimo = self.ultimo.sig
            
    def delNodo(self, valor):
        borrado = False
        temp = self.primero
        if temp != None and temp.valor == valor:
            if self.primero != ultimo:
                self.primero = self.primero.sig
                temp = None
                borrado = True
        if borrado == False:
            while temp.sig != None and borrado == False:
                if temp.sig.valor == valor:
                   temp.sig.sig.atras = temp
                   temp.sig = temp.sig.sig
                   borrado = True
                temp = temp.sig
    
    def recorrerListaAdelante(self):
        temp = self.primero
        while temp != None:
            print str(temp.valor)
            temp = temp.sig

    def recorrerListaAtras(self):
        temp = self.ultimo
        while temp != None:
            print str(temp.valor)
            temp = temp.atras

class listaDeLista():
    primero = None
    ultimo = None
    
    def __init__(self):
        self.ultimo = self.primero = None
        
    def addNodo(self, valor):
        if self.primero == None:
            self.primero = self.ultimo = nodo(valor)
        else:
            self.ultimo.sig = nodo(valor)
            self.ultimo.sig.atras = self.ultimo
            self.ultimo = self.ultimo.sig
            
    def addSubNodo(self, valor, sub_valor):
        temp = self.primero
        while temp != None:
            if temp.valor == valor:
                if temp.der == None:
                    temp.der = nodo(sub_valor)
                else:
                    temp_2 = temp.der
                    while temp_2 != None:
                        if temp_2.der == None:
                            temp_2.der = nodo(sub_valor)
                            break
                        temp_2 = temp_2.der
            temp = temp.sig
            
    def delNodo(self, valor):
        borrado = False
        temp = self.primero
        if temp != None and temp.valor == valor:
            if self.primero != ultimo:
                self.primero = self.primero.sig
                temp = None
                borrado = True
        if borrado == False:
            while temp.sig != None and borrado == False:
                if temp.sig.valor == valor:
                   temp.sig.sig.atras = temp
                   temp.sig = temp.sig.sig
                   borrado = True
                temp = temp.sig
    
    def delSubNodo(self, valor, sub_valor):
        borrado = False
        temp = self.primero
        if temp != None and temp.valor == valor:
            if temp.der != None and temp.der.valor == sub_valor:
                temp.der = temp.der.der
                borrado = True
            if borrado == False:
                temp_2 = temp.der
                while temp_2.der != None:
                    if temp_2.der.valor == sub_valor:
                        temp_2.der = temp_2.der.der
                        borrado = True
                        break
                        
                    temp_2 = temp_2.der
        if borrado == False:
            temp = temp.sig
            while temp != None and borrado == False:
                if temp.valor == valor:
                    if temp.der != None and temp.der.valor == sub_valor:
                        temp.der = temp.der.der
                        borrado = True
                    if borrado == False:
                        temp_2 = temp
                        while temp_2.der != None:
                            if temp_2.der.valor == sub_valor:
                                temp_2.der = temp_2.der.der
                                borrado = True
                                break
                                
                            temp_2 = temp_2.der
                            
                temp = temp.sig
    
    def recorrerListaAdelante(self):
        temp = self.primero
        while temp != None:
            print str(temp.valor)
            temp_2 = temp.der
            if temp_2 != None:
                print "--->",
            while temp_2 != None:
                print str(temp_2.valor) + ",",
                temp_2 = temp_2.der
                
            if temp.der != None:
                print ""
                
            temp = temp.sig

    def recorrerListaAtras(self):
        temp = self.ultimo
        while temp != None:
            print str(temp.valor)
            temp_2 = temp.der
            if temp_2 != None:
                print "--->",
            while temp_2 != None:
                print str(temp_2.valor) + ",",
                temp_2 = temp_2.der
            if temp.der != None:
                print ""
            temp = temp.atras

print "=== Lista normal ==="
print ""
Lista = lista()

Lista.addNodo(3)
Lista.addNodo(55)
Lista.addNodo(77)
Lista.addNodo("32432")

Lista.delNodo(55)

Lista.recorrerLista()

print ""
print "=== Lista doblemente enlazada ==="
ListaDoble = listaDoble()

ListaDoble.addNodo(66)
ListaDoble.addNodo(76)
ListaDoble.addNodo(3312)
ListaDoble.addNodo("87")

ListaDoble.delNodo(76)

print ""
ListaDoble.recorrerListaAdelante()

print ""
ListaDoble.recorrerListaAtras()

print ""
print "=== Lista de listas ==="

ListaDeLista = listaDeLista()

ListaDeLista.addNodo(66)
ListaDeLista.addSubNodo(66, 54234)
ListaDeLista.addSubNodo(66, 7868)
ListaDeLista.addSubNodo(66, 6543)
ListaDeLista.addNodo(76)
ListaDeLista.addSubNodo(76, 44)
ListaDeLista.addSubNodo(76, 54)
ListaDeLista.addSubNodo(76, 6543)
ListaDeLista.addNodo(3312)
ListaDeLista.addSubNodo(3312, 44)
ListaDeLista.addSubNodo(3312, 54)
ListaDeLista.addSubNodo(3312, 534)
ListaDeLista.addNodo("87")

ListaDeLista.delNodo(76)
ListaDeLista.delSubNodo(3312, 54)

ListaDeLista.delSubNodo(66, 54234)

print ""
ListaDeLista.recorrerListaAdelante()

print ""
ListaDeLista.recorrerListaAtras()
