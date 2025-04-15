# -*- coding: utf-8 -*-
"""
Created on Tue Sep 26 22:29:44 2023

@author: Fabio Zangari
"""

res = 2**1000
somma = 0
for i in str(res):
    print(i)
    somma = somma + int(i)
    
print(somma)