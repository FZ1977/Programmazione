# -*- coding: utf-8 -*-
"""
Created on Sat Nov 25 21:33:11 2023

@author: Fabio Zangari
Scrivere una funzione che determini se due parole sono una l'anagramma 
dell'altra.
"""

def Minuscolo(c):
    return chr(ord(c)+32)

def Anagramma(p1, p2):
    d1 = {}
    d2 = {}
    l1 = []
    l2 = []
    
    for i in p1:
        if i >= 'A' and i <= 'Z':
            i = Minuscolo(i)
        
        d1[i] = d1.get(i,0) + 1
        
    for i in p2:
        if i >= 'A' and i <= 'Z':
            i = Minuscolo(i)
            
        d2[i] = d2.get(i,0) + 1
    
    for k,v in d1.items():
        l1.append((k,v))
    
    for k,v in d2.items():
        l2.append((k,v))
    
    l1.sort()
    l2.sort()
    
    if l1 == l2:
        return True
    else:
        return False
    
p1 = "Marea"
p2 = "Remare"
print(Anagramma(p1, p2))