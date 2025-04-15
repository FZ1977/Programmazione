# -*- coding: utf-8 -*-
"""
Created on Wed Jun 29 22:28:43 2022

@author: fabio
"""

def istogramma(x):
    for i in x:
        for n in range(i):
            print('*',end='')
        print()
        
a = [7, 1, 13, 4, 9, 77, 4, 2, 78]

istogramma(a)