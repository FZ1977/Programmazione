# -*- coding: utf-8 -*-
"""
Created on Sat Nov 18 17:02:43 2023

@author: Fabio Zangari
Scrivere una funzione che ordina una lista che contiene 
stringhe e numeri, ponenedo prima i numeri ordinati e poi
le stringhe anche queste ordinate.
"""

def BubbleSortInt(b):
    n = len(b) # lunghezza della lista
    i = 0 # indice
    
    while n>=2:
        for i in range(len(b[:n-1])):
            if abs(b[i]) > abs(b[i+1]):
                b[i], b[i+1] = b[i+1], b[i]
            
        n -= 1
        
def BubbleSortStr(a):
    n = len(a) # lunghezza della lista
    i = 0 # indice
    
    while n>=2:
        for i in range(len(a[:n-1])):
            if a[i] > a[i+1]:
                a[i], a[i+1] = a[i+1], a[i]
            
        n -= 1

def OrdinaLista(l):
    
    a=[] #lista stringhe
    b=[] #lista numeri
    
    for s in l:
        if type(s) == str:
            a.append(s)
        else:
            b.append(s)
            
    BubbleSortStr(a)
    BubbleSortInt(b)
    
    return b+a

a=[3.14,'python',2,'programma',12,0,'corso']
print(OrdinaLista(a))