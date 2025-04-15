# -*- coding: utf-8 -*-
"""
Created on Sun Nov 12 21:01:34 2023

@author: Fabio Zangari
Scrivo una funzione che mergia due liste in una ordinata.
"""

def merge(a, b):
    c = []
    i,j = 0,0
    n = len(a)
    m = len(b)
    
    while i<n and j<m:
        if a[i]<b[j]:
            c.append(a[i])
            i += 1
        if a[i]>b[j]:
            c.append(b[j])
            j += 1
    
    if i==n and j<m:
        c.extend(b[j:])
        
    if j==m and i<n:
        c.extend(a[i:])
                
    return c

a = [3,5,7,9,10,21,34,35]
b = [1,2,6,8,14,16,23]

print(merge(a,b))
