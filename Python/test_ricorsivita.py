# -*- coding: utf-8 -*-
"""
Created on Wed Jun 29 08:58:53 2022

@author: fabio
"""

def somma(x=0):
    if x<10:
        x +=1
    else:
        return 1
        
    return 1 + somma(x)
        
res=somma()
print(res)