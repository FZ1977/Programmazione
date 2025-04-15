# -*- coding: utf-8 -*-
"""
Created on Tue Feb 13 20:42:29 2024

@author: Fabio Zangari
"""

def find_even(L):
    for i in L:
        if i%2 == 0:
            return i
    raise ValueError
        

L = [1,1,1,7]
print(find_even(L))