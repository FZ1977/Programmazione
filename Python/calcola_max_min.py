# -*- coding: utf-8 -*-
"""
Created on Wed Jun 29 08:27:38 2022

@author: fabio
"""

def calcola(n):
    val = []
    for x in range(1,n+1):
        val.append((1/(x+1))**1/2)
    
    return val
    
def max_min(n=2000):
    v_min = min(calcola(n))
    v_max = max(calcola(n))
    
    return v_min, v_max
    
v_min, v_max=max_min()
print('Valore min:',v_min,'Valore max:',v_max)