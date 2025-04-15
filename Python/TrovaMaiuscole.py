# -*- coding: utf-8 -*-
"""
Created on Fri Mar 25 19:14:53 2022

Programma che identificare con tre simboli 
diversi le lettere maiuscole, minuscole ed 
i caratteri numerici.

@author: fabio
"""

a = input('Inserisci una stringa: ')

soluzione = ''

for x in a:
    if x >= 'a' and x <= 'z':
        soluzione += '*' 
    if x >= '0' and x <= '9':
        soluzione += '#'
    if x >= 'A' and x <= 'Z':
        soluzione += '@'
		
print(a)
print(soluzione)	