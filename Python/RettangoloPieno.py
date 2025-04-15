# -*- coding: utf-8 -*-
"""
Created on Fri Mar 25 17:44:43 2022

Disegno su console di un rettangolo con 
un determinato numero di righe e colonne.

@author: fabio
"""

r = 0
c = 0

while r<5:
    if c<10:
        print('*', end='')
        c += 1 
    else:
        print('')
        c = 0
        r += 1