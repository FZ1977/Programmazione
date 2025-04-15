# -*- coding: utf-8 -*-
"""
Created on Sat Jun 25 15:50:33 2022

@author: fabio
"""

def conta(a,d):
    for i in a:
        t=type(i)
        if t==int:
            tipo="Int"
            d[tipo] += 1
        if t==str:
            tipo="Str"
            d[tipo] += 1
        if t==float:
            tipo="Float"
            d[tipo] += 1
        if t==bool:
            tipo="Bool"
            d[tipo] += 1
        if t==tuple:
            tipo="Tuple"
            d[tipo] += 1
            conta(i,d)
        if t==list:
            tipo="List"
            d[tipo] += 1
            conta(i,d)
        if t==dict:
            tipo="Dict"
            d[tipo] += 1
            conta(i,d)
    
    return d


a = [2, 1.6, -1, True, ["«ciao»", 5], "«buonanotte»"]
d={"Int": 0, "Float": 0, "Str": 0, "Bool": 0, "Dict": 0, "List": 0, "Tuple": 0}
d1=conta(a,d)

for k in d1.keys():    
    print(k,":",d1[k])