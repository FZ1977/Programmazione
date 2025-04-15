# -*- coding: utf-8 -*-
"""
Created on Wed Jun 29 10:03:22 2022

@author: fabio
"""

def conta(a):
    b = []    
    for x in a:
        conta=0
        for i in x:
            conta +=1
        
        b.append(conta)
    
    return b

a = ['banana', 'pie', 'Washington', 'book']
print('Lista prodotto con la funzione conta(a):',conta(a))

l_lambda=list(map(lambda x: len(x),a))
print('Lista prodotta con la funzione lambda:',l_lambda)

f_lambda=list(filter(lambda x: len(x)>3, a))
print("Lista di parole con piu' di tre caratteri:",f_lambda)