# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""


def converti_dec_to_bin(a,n_bit,n_dec):
    if n_dec != 1 and n_dec > 0:
        a.append(n_dec%2)
        n_dec=n_dec//2
        return converti_dec_to_bin(a,n_bit,n_dec)
    else:
        a.append(n_dec%2)
        while len(a) < n_bit:
            a.append(0)
        #a.reverse()
        return a
    if n_dec == 0:
        while len(a) < n_bit:
            a.append(0)
        #a.reverse()
        return a
            

a=[]
print(converti_dec_to_bin(a,n_bit=3,n_dec=3))