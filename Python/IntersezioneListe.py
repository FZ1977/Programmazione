# -*- coding: utf-8 -*-
"""
Created on Sat Nov 25 21:06:15 2023

@author: Fabio Zangari
Scrivere una fuznione che prende due liste in ingresso e ritorna una lista
in uscita che è la risultante dell'intersezione delle due liste.
"""

def IntersezioneListe(l1, l2):
    l = []
    for i in l1:
        if i in l2 and i not in l:
            l.append(i)
            
    return l

l1 = [1,2,2,3,4,5,7,8]
l2 = [2,3,3,6,8,9]

print(IntersezioneListe(l1, l2))