# -*- coding: utf-8 -*-
"""
Created on Fri Nov 17 08:08:10 2023

@author: Fabio Zangari
Vari esercizi basati sulle funzioni lambda.
"""
# In[1]
"""
Es. 1
Scrivere una funzione che prenda un parametro e restiruisca 
il quadrato del numero.
"""
quadrato=(lambda x: x**2)
print(quadrato(4))

# In[2]
"""
Es. 2
Scrivere una funzione lambda che prenda una lista e restituisca
una lista di tutti gli elementi della lista originale moltiplicati
per due.
"""
l=[1,2,3,4,5]
doppio=(lambda l: [2*i for i in l])
print(doppio(l))

# In[3]
"""
Es. 3
Scrivere una funzione lambda che prenda una lista di parole e
restituisca una lista contenente solo le parole con che iniziano
con la lettera 'a'.
"""
parole=['ciao','fabio','anatra','Arancia','mandarino','pera','arco']
lista_a=(lambda a: [p for p in a if p[0]=='a' or p[0]=='A'])
print(lista_a(parole))

# In[4]
"""
Es. 4
Scrivere una funzione lambda che prenda due numeri e restituisca la somma
dei loro quadrati.
"""
valore1=2
valore2=3
somma=(lambda a, b: a+b)
print(somma(valore1,valore2))

# In[5]
"""
Scrivere una funzione lambda che prenda una stringa e restituisca True
se la stringa è palindroma.
"""
palindromo=(lambda parola: parola[::-1]==parola)
print(palindromo("ciao"))

# In[6]
"""
Scrivere una funzione lambda che prenda una lista di parole e restituisce
la lunghezza media delle parole nella lista.
"""
a=['ciao','dottore','sorriso','sole','fabio','giallo']
media=(lambda a: sum([len(x) for x in a])/len(a))
print(media(a))

# In[7]
"""
Scrivere una funzione lambda che prenda un lista di numeri e restituisca
la somma solo dei numeri pari.
"""
a=[1,3,2,5,6,76,42,6,65,66,9,7,10]
somma_pari=(lambda a: sum([x for x in a if x%2==0]))
print(somma_pari(a))

# In[8]
"""
Scrivere una funzione lambda che prenda una lista di dizionari e restituisca
una lista di tutte le chiavi dei dizionari.
"""
ld = [{'mela':None, 'pera':None, 'banana':None},{1:'None', 2:'None', 3:'None'},{'a':None, 'b':None, 'c':None},{'alfa':None, 'beta':None, 'gamma':None}]
listaChiavi=(lambda ld: [i.keys() for i in ld])
print(listaChiavi(ld))

# In[9]
"""
Scrivere una funzione lambda che prende una lista di numeri e restituisce
una lista di tutti i numeri maggiorni di 10.
"""
a=[1,3,2,5,6,76,42,6,65,66,9,7,10]
numeriMaggiori=(lambda a: [x for x in a if x > 10])
print(numeriMaggiori(a))

# In[10]
"""
Scrivere una funzione lambda che prende una lista di tuple e restituisca una lista lista di tuple ordinate
per il secondo elemento di ciascuna tupla.
"""
a=[(3,7,5),(2,8,9),(10,40,55),(69,39,17)]
ordinaLista=sorted(a,key=lambda x: x[1])
print(ordinaLista)