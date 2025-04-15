# -*- coding: utf-8 -*-
"""
Created on Sat Mar 26 18:33:58 2022

Precondizione: t è una tna
Restituisce il numero di elementi numerici di t

@author: fabio
"""

def conta_elem_tna( t ):
    if type(t) in (float, int): # t è un numero
        return 1
    else:
        c = 0
        for x in t:
            c += conta_elem_tna( x )
        return c

t = ( 3.14, (2,3), (2.71, (7, 5)), 9, (12, ( 4, )) )

res = conta_elem_tna(t)
print(res)