# -*- coding: utf-8 -*-
"""
Created on Tue Feb  6 20:23:35 2024

@author: Fabio Zangari
"""

minimo, massimo, somma, n = None, None, 0, 0

while True:
    x = float(input("Inserisci numero: "))
    n+=1
    if minimo == None or x < minimo:
        minimo = x
    if massimo == None or x > massimo:
        massimo = x
    
    somma += x
    if n >= 3:
        media = (somma-minimo-massimo)/(n-2)
        print(f"media={media}")