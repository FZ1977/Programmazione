# -*- coding: utf-8 -*-
"""
Created on Sun Nov  5 14:55:36 2023

@author: Fabio Zangari

Date due parole scritte in minuscolo dire se la prima precede la seconda in ordine alfabetico.
La parola più corta precede sempre la più lunga.
"""

parola1 = input("Inserisci la prima parola: ")
parola2 = input("Inserisci la seconda parola: ")

if parola1 < parola2:
    print("Vero")
else:
    print("Falso")