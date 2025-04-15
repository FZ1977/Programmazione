# -*- coding: utf-8 -*-
"""
Created on Sun Mar 27 11:08:56 2022

ALGORITMO: Ricerca Binaria

Ricerca k nella lista a, ritorna la posizione di k in a o -1 se a non contiene k.
Precondizione: a è una lista di elementi ordinati dal più piccolo al più grande

@author: fabio
"""

def bin_search(a, k):
    n = len(a)
    lx, rx = 0, n-1
    while lx <= rx: # fintanto che lo spazio di ricerca non è vuoto
        cx = (lx + rx)//2
        if k == a[cx]:
            return cx
        if k < a[cx]:
            rx = cx-1
        else: # k > a[cx]
            lx = cx+1
    return -1


a = [ 1, 1, 2, 2, 5, 5, 5, 10, 10, 12, 12, 13, 15, 16, 16, 20, 22, 22 ]
print(bin_search(a, 40))
print(bin_search(a, 10))