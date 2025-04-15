# -*- coding: utf-8 -*-
"""
Created on Mon Feb  5 21:37:38 2024

@author: Fabio Zangari
"""

n = int(input('inserisci un valore intero:'))

non_esiste = True

x = 0
y = 2

while x < n and non_esiste:
    y = 2
    while y > 1 and y < 6 and non_esiste:
        if x**y == n:
            print("eccomi")
            non_esiste = False
        y+=1
    x+=1

if non_esiste:
    print("i valori non esistono")
else:
    print(f"valore di x={x-1} e y={y-1}")