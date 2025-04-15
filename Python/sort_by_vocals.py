# -*- coding: utf-8 -*-
"""
Created on Tue Jun 14 18:06:06 2022

Creo una funzione che si chiama sort_by_vocals.


@author: fabio zangari
"""

def Vocali(a):
    v = ('a','e','i','o','u')
    V = ('A','E','I','O','U')
    vocali = [] 
    
    for i in a:
        if(i in v or i in V):
            vocali.append(i)
            
    for j in range(len(vocali)-1):
        for z in range(j+1,len(vocali)):
            if(vocali[j] > vocali[z]):
                temp = vocali[j]
                vocali[j] = vocali[z]
                vocali[z] = temp
    return vocali
     
def Consonanti(a):
    c = ('b','c','d','f','g','h','j','k','l','m','n','p','q','r','s','t','v','w','x','y','z')
    C = ('B','C','D','F','G','H','J','K','L','M','N','P','Q','R','S','T','V','W','X','Y','Z')
    consonanti = []
    
    for i in a:
        if(i in c or i in C):
            consonanti.append(i)
            
    for j in range(len(consonanti)-1):
        for z in range(j+1,len(consonanti)):
            if(consonanti[j] > consonanti[z]):
                temp = consonanti[j]
                consonanti[j] = consonanti[z]
                consonanti[z] = temp    
                
    return consonanti
    
def Numeri(a):
    n = ('0','1','2','3','4','5','6','7','8','9')
    numeri = []    
    
    for i in a:
        if(i in n):
            numeri.append(i)
            
    for j in range(len(numeri)-1):
        for z in range(j+1,len(numeri)):
            if(numeri[j] > numeri[z]):
                temp = numeri[j]
                numeri[j] = numeri[z]
                numeri[z] = temp
                
    return numeri
    
def Speciali(a):
    s = ('*','+','-','/',':','.',',',';','_','=','!','?')    
    speciali = []    
    
    for i in a:
        if(i in s):
            speciali.append(i)
            
    for j in range(len(speciali)-1):
        for z in range(j+1,len(speciali)):
            if(speciali[j] > speciali[z]):
                temp = speciali[j]
                speciali[j] = speciali[z]
                speciali[z] = temp
                
    return speciali

lista = []
a=".pr0grAmMaz1onE-C*"

lista = Vocali(a) + Speciali(a) + Numeri(a) + Consonanti(a)
print(lista)

for i in lista:
    print(i, end="")
    
print()