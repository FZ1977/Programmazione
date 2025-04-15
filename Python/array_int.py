# -*- coding: utf-8 -*-
"""
Created on Tue Jun 14 21:23:09 2022

@author: fabio zangari
"""

def array_int(a):    
    v = ('A','E','I','O','U','a','e','i','o','u')  
    pos = []
    
    for i in range(len(a)):
        for j in range(len(v)):
            if(a[i] == v[j]):
                pos.append(i) 
     
    return pos


a = "Algoritmi"
res = array_int(a)

for i in res:
    print(i, end='')       
    
print()