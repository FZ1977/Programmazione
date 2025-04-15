# -*- coding: utf-8 -*-
"""
Created on Sun Nov  5 16:49:52 2023

@author: Fabio Zangari
Presa una stringa in ingresso sostituiamo ogni spazio con un carattere "_"
"""

s = input("Inserisci una stringa: ")
appo = list(s)
n = len(appo)

for i in range(n):
    if appo[i] == ' ':
        appo[i] = '_'
        
    print(appo[i], end="")