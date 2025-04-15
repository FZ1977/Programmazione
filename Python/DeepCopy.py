# -*- coding: utf-8 -*-
"""
Created on Sat Mar 26 18:36:34 2022

Scrivere una funzione Python denominata 
deep_copy che clona la lista in input e 
tutte le liste annidate che essa contiene.

@author: fabio
"""

def deep_copy( a ):
    if type(a) == list:
        dc_a = []
        for e in a:
            dc_a.append( deep_copy(e) )
        return dc_a
    else:
        return a

a = [ [0, 2], 8, [1, [6, 9], 8], 5 ]
res = deep_copy(a)
print(res)