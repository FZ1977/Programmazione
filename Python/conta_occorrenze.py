# -*- coding: utf-8 -*-
"""
Created on Tue Jun 21 17:10:53 2022

Data una stringa conto quante quante volte sono
ripetuti i vari caratteri.

@author: fabio
"""

def conta_caratteri(a):
    d = {}
    for x in a:
        if x in d:
            d[x] += 1
        else:
            d[x] = 1
   
    d_ord = []
    v_max = max(d.values())

    # ordino l'output dal piu' valore grande al più piccolo
    while(v_max > 0):
        for k, v in d.items():
            if(v == v_max):
                print(k,'-', v)
        v_max = v_max - 1          

a='Stringa di caratteri.'
res=conta_caratteri(a)