# -*- coding: utf-8 -*-
"""
Created on Sun Feb  4 22:21:15 2024

@author: Fabio Zangari
"""

a=input("stringa: ")
b=input("stringa: ")

spazi = (len(a)-len(b))//2

if spazi < 0:
    spazi = -spazi

if len(a) < len(b):
    print(' '*spazi+a)
    print(b)

if len(a) > len(b):
    print(a)
    print(' '*spazi+b)