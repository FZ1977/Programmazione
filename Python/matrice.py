# -*- coding: utf-8 -*-
"""
Created on Sun Jun 26 10:54:32 2022

@author: fabio
"""
def ricerca(a,v):
    r = 0
    c = 0

    for x in m:
        r += 1
        c = 0
        if type(x)==list:
            for i in x:
                c += 1
                if(v==i):
                    print("Il numero",v,"si trova", end=' ')
                    print("Riga",r,"Colonna",c)
        

    print()        
    for x in m:
        if type(x)==list:
            for i in x:
                print(i, end=' ')
            print()
        
        

m = [[1,2,3],[4,5,6],[7,8,9]]
v = int(input('Inserisci il valore da cercare: '))
ricerca(a,v)