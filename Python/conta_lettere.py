# -*- coding: utf-8 -*-
"""
Created on Wed Jun 29 22:31:48 2022

@author: fabio
"""

def conta_lettere(a):
    b = []    
    for x in a:
        b.append(len(x))
    
    return b
    
    
a = ['banana','mignon','elisa','ciao']
print("Questa e' la mia lista:",a)
print(conta_lettere(a))