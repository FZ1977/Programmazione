# -*- coding: utf-8 -*-
"""
Created on Wed Jun 29 22:40:17 2022

@author: fabio
"""

def cerca_elemento(a, n):
    conta = 0    
    
    if n in a:
        print("L'elemento ",n, " e' presente nella lista.")
        for i in a:
            if n==i:
                print("L'elemento si trova nella posizione ",conta)
                
            conta += 1
            

a = [1,4,6,78,23,5,90,5,7,88]
cerca_elemento(a,5)