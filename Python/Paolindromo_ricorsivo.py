# -*- coding: utf-8 -*-
"""
Created on Tue Sep 19 17:47:14 2023

@author: Fabio Zangari
"""

#Verifica se una frase è palindroma

def tutto_minuscolo(f):
    """
    converto la frase con lettere minuscole e cancello tutti gli spazi
    """
    alfabeto={'A':'a','B':'b','C':'c','D':'d','E':'e','F':'f','G':'g','H':'h','I':'i','J':'j','L':'l','M':'m','N':'n','O':'o','P':'p','Q':'q','R':'r','S':'s','T':'t','U':'u','V':'v','W':'w','X':'x','Y':'y','Z':'z'}
    lista=[]
    if type(f) == str:
        for i in f:
            if i in alfabeto.keys():
                lista.append(alfabeto[i])
            elif i == ' ':
                pass
            else:
                lista.append(i)
        
    return lista

def palindromo(l):
    """
    Parameters
    ----------
    l : Funzione
        Verifico se la frase è un palindromo

    Returns
    -------
    True o False

    """
    inizio=0
    fine=len(l)-1
    res = True
    
    if inizio<fine:
        if l[inizio] == l[fine]:
            palindromo(l[inizio+1:fine])
        else:
            res = False
    else:
        res = True
    
    return res

frase=''

print(palindromo(tutto_minuscolo(frase)))

if palindromo(tutto_minuscolo(frase)) == True:
    print("La frase e' un palindromo.")
else:
    print("La frase non e' un palindromo.")