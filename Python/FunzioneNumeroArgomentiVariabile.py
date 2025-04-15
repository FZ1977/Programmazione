# -*- coding: utf-8 -*-
"""
Created on Sat Mar 26 16:21:18 2022

Scrivo un programma per verificare come funzionano le funzioni con
numero di parametri variabili.

@author: fabio
"""

def funzione_test( *argomenti ):
    return argomenti
    
    
res = funzione_test(1,2,3,'ciao', 'sono una stringa', (1,2,3))
print(res)