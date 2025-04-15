# -*- coding: utf-8 -*-
"""
Created on Tue Sep 19 17:26:29 2023

@author: Fabio Zangari
"""

#utilizzo della ricorsione per calcolare il fattoriale di un numero intero positiv o

def fattoriale(x):
    if x == 1:
        return 1
    elif x == 0:
        return 1
    else:
        return x * fattoriale(x-1)


for i in range(0,10):
    print('fattoriale di ',i,'-',fattoriale(i))