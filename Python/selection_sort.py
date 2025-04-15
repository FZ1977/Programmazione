# -*- coding: utf-8 -*-
"""
Created on Mon Jan 30 12:15:24 2023
Algoritmo di ordinamento SELECTION SORT
@author: Fabio Zangari
"""

def selection_sort(a):
    
    for j in range(len(a)-1):
        for i in range(j+1,len(a)):
            print(j, i)
            if(a[j] > a[i]):
                appo=a[j]
                a[j]=a[i]
                a[i]=appo
    
    return a

a=[4,5,1,8,2]
print("Array prima di essere ordinato.")
print(a)
print("Array dopo essere stato ordinato.")
print(selection_sort(a))