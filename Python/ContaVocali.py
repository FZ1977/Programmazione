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
    if s[i] == 'a' or s[i] == 'e' or s[i] == 'i' or s[i] == 'o' or s[i] == 'u' or s[i] == 'A' or s[i] == 'E' or s[i] == 'I' or s[i] == 'O' or s[i] == 'U':
        conta += 1
    
    i += 1
        
print("Il numero vi vocali e': ", conta)