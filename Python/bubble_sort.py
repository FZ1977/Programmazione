# -*- coding: utf-8 -*-
"""
Created on Mon Jan 30 18:15:10 2023
Algoritmo di ordinamento BUBBLE SORT - versione ottimizzata per non fargli fare controlli inutili.
@author: Fabio Zangari
"""

def bubble_sort(a):
    test = False
    
    while (test!=True):
        for i in range(len(a)-1):
            test = True
            if(a[i]>a[i+1]):
                appo = a[i]
                a[i] = a[i+1]
                a[i+1] = appo
                test = False
    
    return a

a=[4,5,1,8,2]
print("Array prima di essere ordinato.")
print(a)
print("Array dopo essere stato ordinato.")
print(bubble_sort(a))