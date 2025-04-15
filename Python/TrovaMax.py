# -*- coding: utf-8 -*-
"""
Created on Sun Nov 12 18:38:49 2023

@author: Fabio Zangari
"""

def rmax(a):
    if len(a) == 1:
        return a[0]
    else:
        m = rmax(a[1:])
        if m>a[0]:
            return m
        else:
            return a[0]
        
        
a=[4,3,6,8,4,9,1]

print(rmax(a))