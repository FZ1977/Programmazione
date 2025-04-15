# -*- coding: utf-8 -*-
"""
Created on Tue Sep 19 21:33:50 2023

@author: Fabio Zangari
"""
def fattoriale(n):
    res=1
    for i in range(1,n+1):
        res = res*i
        
    return res


a=40
b=20
c=20

### Calcolo il numero di permutazini con le ripetizioni n!/n1!*n2!
### dove n è uguale alla somma dei due lati n1+n2. 
res=fattoriale(a)//(fattoriale(b)*fattoriale(c))
print(res)
