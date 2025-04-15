# -*- coding: utf-8 -*-
"""
Created on Mon Apr 11 15:28:15 2022

Calcolo del fattoriale del numero n con la ricorsione.

@author: TL002227
"""

def fattoriale(n, res = 1):
    if(n>=1):
        res = res * n
        res = fattoriale(n-1, res)
    return res
        
print(fattoriale(n=5))