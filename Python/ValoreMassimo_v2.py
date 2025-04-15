# -*- coding: utf-8 -*-
"""
Created on Sat Nov 25 21:17:23 2023

@author: Fabio Zangari
Scrivere una funzione che prende una lista di liste annidate e ritorni il
massimo dei valori.
"""
# %% Programma scritto con ricorsione
def ValoreMassimo(l):
    m = 0
    for i in l:
        if type(i) == list:
            i = ValoreMassimo(i)
        if i > m:
            m = i
            
    return m
            

a = [1,2,[2,3,[4,[5],6],[10,[12]],7,8,9]]

print(ValoreMassimo(a))