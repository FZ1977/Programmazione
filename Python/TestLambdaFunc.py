# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

def test_func(x,y):
    if(y==0):
        return None
    else:
        return x*y

test = lambda x, y: x*y if(y!=0) else None


print("Stampo l'esito della funzione lambda:", test(3,5))
print("Stampo l'esito della funzione tes_func:", test_func(3,6))