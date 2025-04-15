# -*- coding: utf-8 -*-
"""
Created on Sat Mar 26 09:35:34 2022

ALGORITMO: Ricerca per Bisezione
Dato in input un numero x si trova la approssimazione della
sua radice quadrata.

@author: fabio
"""

def radice_quadrata(x, err = 0.0001):
    low, high = 0, max(1,x)
    ans = (low + high)/2
    
    while abs(ans*ans - x) >= err:
        print ('min =', low, 'max =', high, 'ans =', ans)
        if ans*ans < x:
            low = ans
        else:
            high = ans
        ans = (low + high)/2
    return ans
    
x = float(input('Inserisci un valore: '))
res = radice_quadrata(x)
print(res, 'è una approssimazione della radice quadrata di', x)