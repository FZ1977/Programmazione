# -*- coding: utf-8 -*-
"""
Created on Sat Mar 26 10:19:53 2022

ALGORITMO: Ricerca per Bisezione
Dato in input un numero x e definita anche la base b si 
trova l'approssimazione del suo logaritmo in base b.

@author: fabio
"""

def logaritmo(x, b = 10, err = 0.0001):
    low, high = 0, max(1,x)
    ans = (low + high)/2
    
    while abs(b**ans - x) >= err:
        print ('min =', low, 'max =', high, 'ans =', ans)
        if b**ans < x:
            low = ans
        else:
            high = ans
        ans = (low + high)/2
    return ans
    
x = float(input('Inserisci un valore: '))
#b = int(input('Inserisci la base del logaritmo: '))
res = logaritmo(x)
print(res, 'è una approssimazione del logaritmo', x)