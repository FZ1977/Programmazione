# -*- coding: utf-8 -*-
"""
Created on Sun Nov 19 09:37:21 2023

@author: Fabio Zangari
Scrivere una funzione che presa una lista disordinata di 
valori ritorna il valore più grande.
"""

# %% Primo metodo Iterazione
def ValMax(a):
    m = 0
    for i in a:
         if i>m:
             m=i
             
    return m

a=[5,2,8,3,6,4,10,1,0,7,9]
print("Il valore massimo e' -> ",ValMax(a))

# %% Secondo metodo Ricorsione
def ValMax(a,m=0,i=0):
    while i<len(a): # teta(n)
        if a[i]>m: # teta(n)
            m=a[i]
            i += 1
            ValMax(a,m,i)
        else:
            i += 1
    
    return m
        
a=[5,2,8,3,6,4,10,1,0,7,9]
print("Il valore massimo e' -> ",ValMax(a))

# Complessita temporale Teta(n)
# complessita spaziale O(1)

# %% Terzo metodo Ricorsione - scritto dal professore
def ValMax(a):
    if len(a)==1: #caso base
        return a[0]
    else: #caso generale
        m = ValMax(a[1:]) # Questa operazione è costosa
        if m>a[0]: 
            return m
        else:
            return a[0]
        
a=[5,2,8,3,6,4,10,1,0,7,9]
print("Il valore massimo e' -> ",ValMax(a))

# Costo temporale teta(n*n)
# Costo spaziale teta(n*n)

# %% Quarto metodo Ricorsione - meno costoso
def ValMax(a,i=0,m=0):
    if i==len(a)-1: #caso base
        return m
    else: #caso generale
        if a[i]>m:
            m=ValMax(a,i+1,a[i])
        else:
            m=ValMax(a,i+1,m)
    
    return m
        

a=[5,2,8,3,6,4,10,1,0,7,9]
print("Il valore massimo e' -> ",ValMax(a))

# Costo temporale teta(n)
# Costo spaziale teta(n)