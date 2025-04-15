# -*- coding: utf-8 -*-
"""
Created on Wed Jun 29 08:47:13 2022

verifica se una stringa è palindroma: versione iterativa e ricorsiva.

@author: fabio
"""

def palindroma_iter(a):
    dx=len(a)-1
    sx=0    
    
    for i in a:
        if(a[sx]==a[dx]):
            sx += 1
            dx -= 1
        else:
            return 1
        
        if(sx>dx):
            return 0
            
def palindroma_ric(a, sx=0, dx=(len(a)-1)):    
    if(sx>dx):
        return 0

    if(a[sx]==a[dx]):
        sx+=1
        dx-=1
        return 0 + palindroma_ric(a,sx,dx)
    else:
        return 1
    
a="otto"
res=palindroma_iter(a)
if(res==0):
    print("Stringa palindroma - iterativa")
else:
    print("Stringa non palindroma - iterativa")
    
    
res1=palindroma_ric(a)
if(res1==0):
    print("Stringa palindroma - ricorsiva")
else:
    print("Stringa non palindroma - ricorsiva")