# -*- coding: utf-8 -*-
"""
Created on Sat Nov 18 22:02:34 2023

@author: Fabio Zangari
Scrivere una funzione che clona la lista che contiene
liste annidate su vari livelli.
"""

def DeepCopy(a):
    b=[]
    
    for c in a:
        if type(c) == list:
            b.append(DeepCopy(c))
        else:
            b.append(c)
        
    return b

a=[0,[1,2],[3,[4,5],6,[7,[8]]],9]
print(a)
b=DeepCopy(a)
print(b)