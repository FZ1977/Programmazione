# -*- coding: utf-8 -*-
"""
Created on Sun Feb 11 14:51:21 2024

@author: Fabio Zangari
"""

def f(*valori):
    print(valori)
    if len(valori) == 1:
        print(valori[0])
    else:
        print(valori[0]*valori[1])
        

f(3,4)