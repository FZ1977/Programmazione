# -*- coding: utf-8 -*-
"""
Created on Tue Feb  6 21:16:44 2024

@author: Fabio Zangari
"""

n = int(input("Inserisci un numero: "))

a0=1
a1=1
fib = 0

for i in range(n):
    if i == 0 or i == 1:
        print(1)
    else:
        fib = a0 + a1
        a0 = a1
        a1 = fib
        print(fib)