# -*- coding: utf-8 -*-
"""
Created on Sat Jun 25 20:52:56 2022

@author: fabio
"""

d1 = {'Nome':'Marco', 'Cognome':'Verdi', 'Telefono':'782978'}
d2 = {'Indirizzo':'via Dante', 'Telefono':'839434'}
d3 = {}
l = []

for x in d1.keys():
    if x in d2:
        l.append(d1[x])
        d3[x]=l
    else:
        d3[x]=d1[x]
        
for j in d2.keys():
    if j in d1:
        l.append(d2[j])
        d3[j]=l
    else:
        d3[j]=d2[j]
        
for x in d3.keys():
    print(x,":",d3[x])