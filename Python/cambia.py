# -*- coding: utf-8 -*-
"""
Created on Sun Jun 26 11:11:17 2022

@author: fabio
"""

def cambia(t,n):
    d = {1:'uno', 2:'due', 3:'tre', 4:'quattro', 5:'cinque', 6:'sei', 7:'sette', 8:'otto', 9:'nove'}    
    a = []
    for i in range(len(t)):
        if i == 0:
            a.append(d[t[i]])
        else:
            a.append(t[i])
    
    a = tuple(a)
    return a


t = (1,2,3)

res=cambia(t,0)
print(res)