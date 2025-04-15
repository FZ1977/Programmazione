# -*- coding: utf-8 -*-
"""
Created on Fri Mar 25 18:20:29 2022

Creo un programma che gestisce eccezioni

@author: fabio
"""

try:
    3/0
except ZeroDivisionError:
    print('Non è possibile dividere per zero un numero.')
    
try:
    int(a)
except NameError:
    print('Variabile non definita.')
