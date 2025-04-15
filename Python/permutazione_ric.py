<<<<<<< HEAD
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 29 14:16:28 2023

@author: Fabio Zangari
"""

def  permutazione(s,i):
    if s==[1,3,2]:
        return s
    if len(s)==0:
        return s
    else:
        print(s)
        temp=s[i]
        s[i]=s[i+1]
        s[i+1]=temp
        if i<1:
            permutazione(s,i+1)
        else:
            i=0
            permutazione(s,i)

s=[1,2,3]
print(permutazione(s,0))
=======
def permutazione(stringa):
    if len(stringa) < 1:
        return stringa
    elif len(stringa) == 2:
        return [stringa, stringa[1]+stringa[0]]
    lista_permutazioni=[]
    for i in range(len(stringa)):
        carattere_fisso=stringa[i]
        stringa_parziale = stringa[0:i]+stringa[i+1:]
        if len(stringa_parziale) > 2:
            intermedia=permutazione(stringa_parziale)
            for index in range(len(intermedia)):
                intermedia[index]=carattere_fisso+intermedia[index]
            lista_permutazioni += [intermedia]
        else:
            lista_permutazioni += [carattere_fisso + stringa_parziale]
            lista_permutazioni += [carattere_fisso + stringa_parziale[1] + stringa_parziale[0]]
    return lista_permutazioni        
            

stringa="12345"

print(permutazione(stringa))
>>>>>>> 270528f19efb9186c940a381c0121f3283c3b3ec
