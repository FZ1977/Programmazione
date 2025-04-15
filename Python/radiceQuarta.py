# -*- coding: utf-8 -*-
"""
Created on Fri Nov 17 15:26:37 2023

@author: Fabio Zangari
Si scriva una funzione che calcoli la radice quarta del numero inserito.
"""

"""
Ho dovuto applicare questa soluzione perchè se utilizzavo
il controllo per x**4 arrivavo ad un punto dell'algoritmo
che mi portava ad un loop infinito.
"""

def radiceQuadrata(x):
    e = 0.0000001
    g=x

    while abs(x - g**2) > e:
        g=0.5*(g + x/g)
        print(g)
        
    return g

x=17

print(radiceQuadrata(radiceQuadrata(x)))