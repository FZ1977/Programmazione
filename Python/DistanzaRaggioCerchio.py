# -*- coding: utf-8 -*-
"""
Created on Tue Feb  6 20:15:22 2024

@author: Fabio Zangari
"""

x=int(input("inserisci x: "))
y=int(input("inserisci y: "))

r = 10

diag = ((x**2)+(y**2))**(0.5)

if diag <= r:
    print("Interno")
else:
    print(f"{diag - r}")