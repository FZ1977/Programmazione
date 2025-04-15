# -*- coding: utf-8 -*-
"""
Created on Sun Feb  4 23:01:28 2024

@author: Fabio Zangari
"""

a=input("stringa: ")
n = len(a)
test = True
for i in a:
    if i >= '0' or i <= '9':
        pass
    else:
        test = False

punto=0
s=''
if test:
    #e' un numero
    while n > 0:
        s = a[n-1]+s
        n-=1
        punto +=1
        
        if punto == 3:
            s = "."+s
            punto=0
            
print(s)