# -*- coding: utf-8 -*-
"""
Spyder Editor

Calcolo della radice quadrata.
"""

x = 20
g = x
while abs(g*g-x) > 0.00001:
    print(g)
    g = 0.5*(g+x/g)
    
print(g)