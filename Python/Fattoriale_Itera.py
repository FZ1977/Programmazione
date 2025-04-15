# -*- coding: utf-8 -*-
"""
Created on Mon Apr 11 14:08:31 2022

Calcolo del fattoriale del numero n con l'iterazione.

@author: TL002227
"""

n = 100
res = 1

while(n>=1):
    res = n*res
    n -= 1

print(res)