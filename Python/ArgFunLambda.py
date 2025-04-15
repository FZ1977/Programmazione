# -*- coding: utf-8 -*-
"""
Created on Sun Feb 11 16:47:36 2024

@author: Fabio Zangari
"""

def find_max(x,y,z,key=lambda x: x):
    v_max = key(x)
    if key(y) > v_max:
        v_max = y
    elif key(z) > v_max:
        v_max = z
    else:
        v_max = x
    return v_max

print(find_max(-2,16,-1, key=lambda x: -x))
#deve restituire -1;

print(find_max('programma', 'python', 'algoritmo'))
#deve restituire python;

print(find_max('programma', 'python', 'algoritmo', key=len))