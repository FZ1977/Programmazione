# -*- coding: utf-8 -*-
"""
Created on Sun Nov  5 17:08:20 2023

@author: Fabio Zangari
Palindromo di una stringa.
"""

def Palindromo_v1( s ):
    appo = ''
    for c in s:
        appo = c + appo
    
    if s == appo:
        return True
    else:
        return False

def Palindromo_v2( s ):
    appo = []
    s = list(s)
    
    n = len(s)
    
    appo = s[::-1]
    
    # Forma più costosa
    #for i in range(n-1,-1,-1):
    #    appo.append(s[i])
        
    if s == appo:
        return True
    else:
        return False
    
    
s = input("Inserisci stringa: ")

if Palindromo_v1(s) == True:
    print(s + " e' palindromo.")
else:
    print(s + " non e' un palindromo.")
    
if Palindromo_v2(s) == True:
    print(s + " e' palindromo.")
else:
    print(s + " non e' un palindromo.")