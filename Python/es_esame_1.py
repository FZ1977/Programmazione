# -*- coding: utf-8 -*-
"""
Created on Thu Jun 16 18:10:37 2022

@author: fabio
"""

k = ''
n0 = 5
n1 = 7
d0, d1 = {}, {}
for i in range(20):
    d0[k+'x'] = i
    d1[i] = k + 'x'
    k += 'x'

print(d0)
print(d1)
print(d0[d1[n0]+d1[n1]])