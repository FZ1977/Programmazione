# -*- coding: utf-8 -*-
"""
Created on Fri Nov 17 21:20:46 2023

@author: Fabio Zangari
Scrivere una funzione che conta quante volte
una stringa x compare in una stringa y.
"""

def TrovaOccorrenzaStr(stringa1, stringa2):
    conta = 0
    n = len(stringa1)
    m = len(stringa2)
    j = 0

#Questa è l'algoritmo più smart    
    for i in range(n):
        if stringa1[i:i+m] == stringa2:
            conta += 1
            
    return conta

"""
Questa è la forma più complessa del programma.
    
    for i in range(n):
        if j<m:
            if stringa2[j] == stringa1[i]:
                j += 1
            else:
                j = 0
        
        if j==m:
            conta += 1
            j = 0
    return conta                
"""

stringa1='supercalifragilistichespiralitoso'
stringa2='ali'

print(TrovaOccorrenzaStr(stringa1,stringa2))