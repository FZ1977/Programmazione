# -*- coding: utf-8 -*-
"""
Created on Sun Nov  5 14:42:12 2023

@author: Fabio Zangari
Voglio contare quante vocali ci sono nella stringa inserita.
"""

s = input("Inserisci una stringa: ")
i = 0 # indice della stringa
n = len(s) # numero di caratteri di una stringa
conta = 0 # numero delle vocali

while i<n:
    if s[i] in 'aeiouAEIOU':
        conta += 1
    
    i += 1
        
print("Il numero vi vocali e': ", conta)