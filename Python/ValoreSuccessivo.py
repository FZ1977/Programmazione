# -*- coding: utf-8 -*-
"""
Created on Sun Nov  5 16:28:41 2023

@author: Fabio Zangari
Scrivo un funzione che prende in ingresso un valore e ritorna il suo valore successivo
"""

def ValoreSuccessivo( x ):
    
    i = 0 # indice
    n = len(x) # lunghezza stringa
    
    while i<n:
        if x[i] not in '0123456789':
            print("Non e' un valore numerico.")
            return 
        i += 1
    
    return int(x)+1

x = input("Inserisci un valore numerico: ")

print(ValoreSuccessivo(x))