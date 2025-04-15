# -*- coding: utf-8 -*-
"""
Created on Mon Feb  5 21:46:11 2024

@author: Fabio Zangari
"""

somma = 0
primo = 0

for n in range(3,1000):
    for x in range(2,n+1):
        if n%x == 0:
            primo+=1
            
    if primo == 1:
        somma = somma + n
        primo = 0
    else:
        primo = 0
        
print(f"somma dei primi mille numeri primi = {somma}")
        