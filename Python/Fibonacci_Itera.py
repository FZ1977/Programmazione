# -*- coding: utf-8 -*-
"""
Created on Mon Apr 11 13:54:54 2022

Algoritmo per calcolare la successione di fibonacci dei primi 100 numeri utilizzando l'iterazione.

@author: TL002227
"""

def fibonacci(a, b):
    f = a + b
    while (f < 1000000):
        print(f, end=" ")
        a = b
        b = f
        f = a + b

a=0
b=1
print(a, b, end=" ")    
fibonacci(0,1)