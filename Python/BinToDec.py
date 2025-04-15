# -*- coding: utf-8 -*-
"""
Created on Mon Feb  5 22:13:20 2024

@author: Fabio Zangari
"""

binario = 0
x = '10011'
n = 0
for i in x[::-1]:
    binario = binario + (int(i)*(2**n))
    n+=1

print(binario)