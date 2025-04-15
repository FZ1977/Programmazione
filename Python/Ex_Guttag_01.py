# -*- coding: utf-8 -*-
"""
Created on Sun Apr 14 21:47:59 2024
Scrivere un programma che chidede all'utente di inserire 10 numeri
interi e riporta in output solo il numero dispari più grande.
Se non sono inseriti numeri dispari in ingresso allora deve
scrivere che non sono stati inseriti numeri dispari.
@author: Fabio Zangari
"""

max_dispari = 0
n = 10

while n>0:
    x = int(input("Inserisci un numero intero: "))
    if x%2 != 0:
        if x > max_dispari:
            max_dispari = x
    n = n - 1
    
if max_dispari == 0:
    print("Non sono stati inseriti numeri dispari")
else:
    print(max_dispari, "e' il numero dispari piu' grande inserito")
