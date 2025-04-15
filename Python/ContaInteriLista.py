# -*- coding: utf-8 -*-
"""
Created on Sun Nov 19 10:53:39 2023

@author: Fabio Zangari
Scrivere una funzione che conti il numeri di interi contenuti
in una lista che contenga liste annidate.
"""

def ContaInteri(a,n=0):
    for i in a:
        if type(i)==list:
            n = ContaInteri(i,n)
        else:
            n=n+1
    
    return n

a=[0,[1,[2,3,[4,5],6],7,8,[9]]]
print("Il numero di interi nella lista e':", ContaInteri(a))