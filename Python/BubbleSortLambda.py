# -*- coding: utf-8 -*-
"""
Created on Sat Mar 26 21:35:52 2022

@author: fabio
"""

def bubble_sort( a, lambda x, y: x<=y ):
    n = len(a)
    ordinata = False
    num_scansioni = 0 # numero di scansioni (esecuzioni for) già eseguite
    while not ordinata:
        ordinata = True
        for i in range(n-1-num_scansioni):
            # confrontiamo l'elemento in posizione i e i+1
            if not cmp_func(a[i], a[i+1]) :
                # scambio gli elementi, non posso dire che la lista è ordinata
                a[i], a[i+1] = a[i+1], a[i]
                ordinata = False
        num_scansioni += 1
        
a = [6, 'zero', 'novantanove', 2, 'tre', 0, 'uno', 3.14]
bubble_sort(a)
print(a)