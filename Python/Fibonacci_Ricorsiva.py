# -*- coding: utf-8 -*-
"""
Created on Mon Apr 11 11:22:43 2022

Algoritmo per calcolare la successione di fibonacci dei primi 100 numeri utilizzando la ricorsione.

@author: TL002227
"""

def fibonacci(a, b):
    f = a + b
    print(f, end=" ")
    a = b
    b = f
    if(f < 1000000):    
        fibonacci(a, b)
    else:
        return f

a=0
b=1
print(a, b, end=" ")    
fibonacci(0,1)