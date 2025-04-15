# -*- coding: utf-8 -*-
"""
Created on Tue Jun 14 21:39:43 2022

@author: fabio zangari
"""

def rimuovi_stringa(a,b):
    a = list(a)
    b = list(b)
    len_a = len(a)
    len_b = len(b)
    j = 0    
    
    
    for i in range(len_a):
        if(a[i] == b[j]):
            j += 1
            if(j == len_b):
                pos_finale = i
                pos_iniziale = pos_finale - len_b
				
                for i in range(pos_iniziale+1, pos_finale+1):
                    a[i] = ''
				
                for i in range(len_a):
                    print(a[i],end='')
                print()
                return 1
        else:
            j = 0
    
    return 0

a = "programmazione dei calcolatori"
b = "azione"

res = rimuovi_stringa(a,b)
print(res)