# -*- coding: utf-8 -*-
"""
Created on Tue Feb  6 21:04:10 2024

@author: Fabio Zangari
"""

a0=1
b0=(0.5)**0.5
p0=1
q0=0.25

for i in range(10):
    a=(a0+b0)/2
    b=(a0*b0)**(0.5)
    p=2*p0
    q=q0-p0*(a0-a)**2

    a0=a
    b0=b
    p0=p
    q0=q

    pi=((a+b)**2)/(4*q)
    print(pi)
    
#%%Prof
a, b, q, p = 1, 1/(2**0.5), 1/4, 1

for i in range(10):
    temp = a
    a = (temp+b)/2
    b = (temp*b)**0.5
    q = q-p*(temp-a)**2
    p = 2*p
    pi = ((a+b)**2)/(4*q)
    print(pi)