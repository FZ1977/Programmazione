# -*- coding: utf-8 -*-
"""
Created on Sun Nov 19 11:21:18 2023

@author: Fabio Zangari
Scrivere una funzione che esegue la ricerca di un valore
in una lista non ordinata e senza ripetizioni.
"""

# %% Primo algoritmo di ricerca
def RicercaValore(a,v):
    if v in a:
        return v
    else:
        return None

a=[23,6,87,4,21,32,97,3,2,7,9]
v=90
if RicercaValore(a, v)==None:
    print(v,"non presente nella lista")
else:
    print(v,"presente nella lista")
    
# Se la ricerca e' una sola allora non ci sono problemi
# di prestazioni. Il suo costo p:
# costo spaziale O(1)
# costo temporale O(n)
    
# %% Secondo algoritmo di ricerca
def MergeSort(a):
    if len(a)>1:
        a_sx = a[:len(a)//2]
        a_dx = a[len(a)//2:]
        MergeSort(a_sx) # valore di sinistra
        MergeSort(a_dx) # valore di destra
        
        # Merge
        i, j, k = 0, 0, 0
        while i < len(a_sx) and j < len(a_dx):
            if a_sx[i] > a_dx[j]:
                a[k] = a_dx[j]
                j += 1
                k += 1
            else:
                a[k] = a_sx[i]
                i += 1
                k += 1
                
        while i < len(a_sx):
            a[k] = a_sx[i]
            i += 1
            k += 1
        
        while j < len(a_dx):
            a[k] = a_dx[j]
            j += 1
            k += 1

def BinSearch(a,v):
    if len(a)>1:
        a_cx = a[len(a)//2]
        if v == a_cx:
            print(v,"valore presente")
        if v > a_cx:
            a = a[:len(a)//2]
            BinSearch(a,v)
        else:
            a = a[len(a)//2:]
            BinSearch(a,v)
    if len(a) == 1:
        if a[0] == v:
            print(v,"valore prsente")
        else:
            print(v,"valore non presente")
        
    

a=[23,6,87,4,21,32,97,3,2,7,9]
MergeSort(a)
for i in range(101):
    BinSearch(a, v)
  
# Con questo algoritmo posso cercare 