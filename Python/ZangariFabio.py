# -*- coding: utf-8 -*-
"""
Created on Mon Jun 20 12:13:29 2022

Si scriva una funzione Python, denominata sort_by_occurrences, 
che prende in input una stringa e restituisce una nuova 
stringa in cui i caratteri di quella originale risultino 
ordinati dal meno frequente al più frequente.

Ad esempio, se
a = ')-:))-'
sort_by_occurrences( a ) deve ritornare
':-)'

@author: fabio zangari
"""

def sort_by_occurrences(a):
    d={}    
    for x in a:
        if (x not in d):
            d[x] = 0
        else:
            d[x] += 1
    
    for x in sorted(d.keys(), reverse=True):
        print(x, end='')
    
    print()