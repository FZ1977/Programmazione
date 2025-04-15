# -*- coding: utf-8 -*-
"""
Spyder Editor
Prende in input un insieme di parole, torna la lista ordinata di 
tutte le parole che è possibile creare fondendo le parole 
nell'insieme di partenza.
"""

a=input("stringa: ")
b=input("stringa: ")

test = True
x = 0
y = 0

while test and x < len(a):
    y = 0
    while test and y < len(b):
        if a[x] == b[y]:
            test = False
        else:
            y+=1
        x+=1


for s in (b[:y]):
    print(" "*(x-1)+s)
print(a)
for s in (b[y+1:]):
    print(" "*(x-1)+s)