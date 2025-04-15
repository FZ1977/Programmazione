# -*- coding: utf-8 -*-
"""
Created on Sun Mar 27 15:50:20 2022
ALGORITMO: MERGE SORT.

Precondizione: a una lista numerica
Ordina a[lx:rx]
    
@author: fabio
"""

def merge_sort(a, lx, rx):
    '''
    Precondizione: a una lista numerica
    Ordina a[lx:rx]
    '''
    
    if lx <= rx-2: # almeno due elementi in a[lx:rx]
        cx = (rx+lx)//2
        merge_sort(a, lx, cx)
        merge_sort(a, cx, rx)
        a = merge(a, lx, cx, rx)

#con questa prova non funziona
a = [4,2,3,7,4,3,4,5,2,3,0,9,5,4,8]
n = len(a)
merge_sort(a, 0, n)
print(a)

