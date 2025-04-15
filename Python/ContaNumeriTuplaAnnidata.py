# -*- coding: utf-8 -*-
"""
Created on Tue Feb 13 20:29:43 2024

@author: Fabio Zangari
"""

def f(t):
    somma = 0
    for i in t:
        if type(i) == int or type(i) == float:
            somma += 1
        else:
            somma += f(i)
            
    return somma

t = ( 3.14, (2, 3), (2.71, (7, 5)), 9, (12, ( 4, )) )

print(f(t))