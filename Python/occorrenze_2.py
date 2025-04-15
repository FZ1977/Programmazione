# -*- coding: utf-8 -*-
"""
Created on Wed Jun 29 22:35:31 2022

@author: fabio
"""

def conta_occorrenze(a):
    d = {}
    for x in a:
        if x in d:
            d[x] += 1
        else:
            d[x] = 1

    return d

a = "ababcccddnnmsowsaedklsa2"
print(conta_occorrenze(a))