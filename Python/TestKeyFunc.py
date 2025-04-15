# -*- coding: utf-8 -*-
"""
Created on Sat Mar 26 20:58:46 2022

@author: fabio
"""

def cmp_len( x, y):
    # restituisce l'esito del confronto tra le lunghezze degli argomenti
    return len(x) <= len(y)

def cmp_val( x, y):
     # restituisce l'esito del confronto tra i valori dei argomenti
    return x <= y

def compara(a, cmp_func = cmp_val):
    if cmp_func(a[0], a[1]):
        return True
    else:
        return False
        
        
a = ['ciao','lungo']
if type(a[0]) in (int, float) and type(a[1]) in (int, float):
    res = compara(a, cmp_val)
else:
    res = compara(a, cmp_len)
    
print(res)