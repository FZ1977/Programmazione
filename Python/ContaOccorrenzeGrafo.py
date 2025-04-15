# -*- coding: utf-8 -*-
"""
Created on Sat Nov 25 17:05:56 2023

@author: Fabio Zangari
"""

def Minuscolo(c):
    return chr(ord(c)+32)

def Draw(l):
    massimo = l[0][1]
    
    for x in l:
        n = (50*x[1]) // massimo 
        print("%6d" % x[1] ,'-',n*'#') # Allineo a destra
    #121052 : 50 = 116251 : x
    
    

def CreaLista(d):
    l = []
    for k,v in d.items():
        l.append((k,v))
    
    l.sort(key=(lambda l: l[1]),reverse=True)
    Draw(l)

def CreaDizionario(f):
    d = {}
    for linea in f:
        for p in linea.split():
            for c in p:
                if c >= 'a' and c <= 'z':
                    d[c] = d.get(c,0) + 1
                if c >= 'A' and c <= 'Z':
                    c=Minuscolo(c)
                    d[c] = d.get(c,0) + 1
                if c == 'è' or c == 'é':
                    d['e'] = d.get('e',0) + 1
                if c == 'ù':
                    d['u'] = d.get('u',0) + 1
                if c == 'ò':
                    d['o'] = d.get('o',0) + 1
    CreaLista(d)




f = open('C:\\Users\\LENOVO\\Desktop\\Git\\Python\\CorsoProgrammazionePython\\i_promessi_sposi.txt','r')
CreaDizionario(f)