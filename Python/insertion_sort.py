# -*- coding: utf-8 -*-
"""
Created on Mon Jan 30 16:06:36 2023
Algoritmo di ordinamento INSERTION SORT
@author: Fabio Zangari
"""

def insertion_sort(a):
    for i in range(1,len(a)):
        if(i>1):
            if(a[i]<a[i-1]):
                appo=a[i]
                a[i]=a[i-1]
                a[i-1]=appo
                x=i-1
                while(x>=1):
                    if(a[x]<a[x-1]):
                        appo=a[x-1]
                        a[x-1]=a[x]
                        a[x]=appo
                    x-=1
        else:
            if(a[i]<a[i-1]):
                appo=a[i]
                a[i]=a[i-1]
                a[i-1]=appo
    return a
                

a=[12,5,3,4]
print("Array prima di essere ordinato.")
print(a)
print("Array dopo essere stato ordinato.")
print(insertion_sort(a))