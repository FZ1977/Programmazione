# -*- coding: utf-8 -*-
"""
Created on Fri Sep 15 11:05:32 2023

@author: Fabio Zangari
"""

def numero_primo(n):
    conta = 0
    for x in range(1,n+1):
        if n%x == 0:
            conta = conta + 1
            if conta > 2 :
                return False
        
    if conta == 1:
        return False
    elif conta == 2:
        return True

res = 0
for i in range(0,2000001):
    if numero_primo(i) == True:
        print(i,"e' un numero primo.")
        res = res + i
        

print(res)