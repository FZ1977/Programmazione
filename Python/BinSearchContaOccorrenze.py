# -*- coding: utf-8 -*-
"""
Created on Sun Mar 27 11:13:15 2022

Data una lista a di n interi ordinati 
dal più piccolo al più grande ed un 
intero k, scrivere una funzione che 
restituisce il numero di elementi in a 
minori o uguali a k. 

Il costo deve essere O(log n)

@author: fabio
"""

def conta_occorrenze(a, k):
    n = len(a)
    lx = 0
    rx = n-1
    
    while lx <= rx:
        cx = (lx + rx)//2
        if k >= a[cx] and ( cx == n-1 or a[cx+1] > k ):
            return cx+1
        if k < a[cx]:
            rx = cx-1
        else: # k > a[cx]
            lx = cx+1
    return 0
            

a = [ 1, 1, 2, 2, 5, 5, 5, 10, 10, 10, 12, 12 ]
res = conta_occorrenze(a, 10)
print(res)