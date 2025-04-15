# -*- coding: utf-8 -*-
"""
Created on Fri Mar 25 22:32:29 2022

Scrivere una funzione che prende in input 
una stringa e restituisce *True* se questa 
è palindroma, *False* altrimenti.

@author: fabio
"""

def palindroma(a):
    a_pal = a[::-1]
    if a == a_pal:
        return True
    else:
        return False

a = input('Inserisci una stringa: ')

res = palindroma(a)
print(res)