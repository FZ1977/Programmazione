# -*- coding: utf-8 -*-
"""
Created on Sat Mar 26 16:28:26 2022

scrivere una funzine ricorsiva che 
restituisce True se e solo se la stringa 
in input è palindroma.

@author: fabio
"""

def palindroma(a):
    n = len(a)
    
    print(a)
    if n > 2:
        if a[0] == a[n-1]:
            palindroma(a[1:n-1])
            return True
        else:
            return False


a = input('Inserisci una parola: ')
res = palindroma(a)
print(res)