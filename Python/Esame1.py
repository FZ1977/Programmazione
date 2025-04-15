# -*- coding: utf-8 -*-
"""
Created on Sat Jan 20 22:16:29 2024

@author: Fabio Zangari
"""

def f(a,b):
    if b in a:
        start = a.index(b)
        print(a[:start]+a[len(b)+start:])
        return 1
    else:
        return 0

a = "programmazione dei calcolatori"
b = "azione"

print(f(a,b))