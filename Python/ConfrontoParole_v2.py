# -*- coding: utf-8 -*-
"""
Created on Sun Nov  5 14:55:36 2023

@author: Fabio Zangari

Date due parole scritte in minuscolo dire se la prima precede la seconda in ordine alfabetico.
La parola più corta precede sempre la più lunga.
"""

s1 = input("Inserisci la prima parola: ")
s2 = input("Inserisci la seconda parola: ")
n1 = len(s1) # teta(n)
n2 = len(s2) # teta(n)

ret = 'Vero' # variabile sentinella O(1)

i = 0 # indice della parola

while i < min(n1,n2):
    if s1[i] <= s2[i]: # O(min(n1,n2))
        i += 1 # O(1)
    else:
        ret = 'Falso' # O(1)
        i += 1 # O(1)
        
print(ret)