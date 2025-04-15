# -*- coding: utf-8 -*-
"""
Created on Sat Mar 26 17:25:40 2022

ALGORITMO: BUBBLE-SORT (ottimizzato)
pre: a e' una lista di numeri
e li ordina dal più piccolo al piu grande

@author: fabio
"""

def bubble_sort( a ):
    '''
    pre: a è una lista di numeri
    l'algoritmo sposta il valore più grande all'ultimo
    posto della lista e lascia gli altri elementi 
    '''
    n = len(a)
    ordinata = False
    num_scansioni = 1
    while not ordinata:
        ordinata = True
        for i in range(n-1):
            # confrontiamo l'elemento in posizione i e i+1
            if a[i] > a[i+1]:
                # scambio gli elementi, non posso dire che la lista è ordinata
                a[i], a[i+1] = a[i+1], a[i]
                ordinata = False
        return a

a = [9,8,7,6,5,4,3,2,1]
res = bubble_sort(a)
print(res)