# -*- coding: utf-8 -*-
"""
Created on Sun Nov 19 11:28:50 2023

@author: Fabio Zangari
Algoritmo di ordinamento MergeSort.
"""

def Merge(a,a_sx,a_dx):
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


def MergeSort(a):
    if len(a)>1:
        a_sx = a[:len(a)//2]
        a_dx = a[len(a)//2:]
        MergeSort(a_sx) # valore di sinistra
        MergeSort(a_dx) # valore di destra
        Merge(a,a_sx,a_dx)

    
a=[23,6,87,4,21,32,97,3,2,7,9]
print(a)
MergeSort(a)
print(a)