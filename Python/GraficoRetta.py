# -*- coding: utf-8 -*-
"""
Created on Sun Feb 11 14:25:49 2024

@author: Fabio Zangari
"""

m = 3
q = 2

for x in range(40):
    print("-",end="")

print("-> y")

for x in range(11):
    y = m*x + q
    print("|"+y*" "+"*")

print("|")
print("V")
print("x")