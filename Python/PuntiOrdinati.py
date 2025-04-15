# -*- coding: utf-8 -*-
"""
Created on Sat Nov 18 14:34:41 2023

@author: Fabio Zangari
Scrivere una funzione che data una lista di punti ordini
la lista in base alla distanza dal centro di questa.
"""

def OrdinaLista(p, n):
    m = len(p)
    i = 0
    
    while m>=2:
        while i<m-1:
            if p[i]>p[i+1]:
                p[i], p[i+1] = p[i+1], p[i]
                n[i], n[i+1] = n[i+1], n[i]
                i += 1
            else:
                i += 1
            
        i = 0
        m -= 1

def Draw(p, n):
    for i in p:
        print(i, end=" ")

    print()

    for i in range(len(p)):
        if len(p)%2 == 0:
            if i == len(p)//2 - 1:
                print("*", end=" ")
            elif i == len(p)//2:
                print("*", end=" ")
            else:
                print("+", end=" ")
        else:
            if i == len(p)//2:
                print("*", end=" ")
            elif i == len(p)//2+1:
                print("*", end=" ")
            else:
                print("+", end=" ")

    print()

    for i in n:
        print(i, end=" ")

p = [2,0,6,9,7,3]
n = ['B','A','D','F','E','C']

OrdinaLista(p, n)
Draw(p,n)



 