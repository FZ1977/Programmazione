# -*- coding: utf-8 -*-
"""
Created on Sun Feb 11 15:49:50 2024

@author: Fabio Zangari
"""

def is_in(a,b):
    n_a = len(a)
    n_b = len(b)
    
    if n_a > n_b:
        for i in range(n_a-n_b+1):
            if a[i:i+n_b] == b:
                print(i)
    else:
        for i in range(n_b-n_a+1):
            if b[i:i+n_a] == a:
                print(i)
                
is_in('noce','rinoceronte')