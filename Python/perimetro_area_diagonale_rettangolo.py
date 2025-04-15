# -*- coding: utf-8 -*-
"""
Created on Sun Oct 15 10:48:50 2023

@author: Fabio Zangari
"""
from math import sqrt

def Perimetro(latoA, latoB):
    return (2*latoA)+(2*latoB)

def Area(latoA, latoB):
    return (latoA*latoB)

def Diagonale(latoA, latoB):
    return sqrt((latoA*latoA)+(latoB*latoB))

latoA=int(input("lato A: "))
latoB=int(input("lato B: "))

print("Perimetro: ",Perimetro(latoA,latoB))
print("Area: ",Area(latoA,latoB))
print("Diagonale: ",Diagonale(latoA,latoB))