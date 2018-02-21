# -*- coding: utf-8 -*-

"""

    Programa desarrollado por el Licenciado César Cordero Rodríguez.
    Bajo licencia GPLv3.
    Puede ser modificado, copiado y distribuido.
    Se desarrolló con fines educativos.

"""

# Brackets balanced: In a string, the program will check the pair's balance of
#                    []{}(), and the correct order, using stacks.

import time

def pairs_stack(string, pairs = {'[': ']', '{': '}', '(': ')'}):
    
    opening = pairs.keys()
    
    closing = pairs.values()
    
    match = list()
    
    for s in string:
        if s in opening:
            match.insert(0, s)
        elif s in closing:
            if len(match) == 0:
                return False
            if match[0] == opening[closing.index(s)]:
                match.pop(0)
            else:
                return False
    
    if len(match) == 0:
        return True
    
    return False

millis = float(time.time() * 1000)

string = "[]{}()[][][]"
print "Should be true"
print str(pairs_stack(string))

string = "([()][][{}])"
print "Should be true"
print str(pairs_stack(string))

string = "[(])"
print "Should be false"
print str(pairs_stack(string))

string = "[([])()({})]"
print "Should be true"
print str(pairs_stack(string))

string = "[(,,),(,,[])]"
print "Should be true"
print str(pairs_stack(string))

string = "[(,,,(,,[])]"
print "Should be false"
print str(pairs_stack(string))

string = "]"
print "Should be false"
print str(pairs_stack(string))

string = "["
print "Should be false"
print str(pairs_stack(string))

string = "{[{}][][({})]}"
print "Should be true"
print str(pairs_stack(string))

string = """
    public static void main(String args[])
    {
        System.out.println("Hello world");
    }
"""

print "Should be true"
print str(pairs_stack(string))

string = "[[[((({{{}}})))]]]"

print "Should be true"
print str(pairs_stack(string))

millis = float(time.time() * 1000) - millis
print "Result " + str(millis)
