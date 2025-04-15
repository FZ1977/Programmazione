# -*- coding: utf-8 -*-
"""
Created on Sat Mar 26 21:43:14 2022

pre: a è una lista
Ordina gli elementi della lista in modo crescente rispetto ai valori  
restituiti dalla funzione k. Ovvero dopo l'esecuzione della funzine se
a = [a_0, a_1,... a_n] allora k(a_i) <= k(a_i+1) per tutti gli i.
Di default k è la funzione identità 

@author: fabio
"""

def bubble_sort( a, k = lambda x: x, reverse = False):
    s = 1 if reverse == False else -1
    
    n = len(a)
    ordinata = False
    num_scansioni = 0 # numero di scansioni (esecuzioni for) già eseguite
    while not ordinata:
        ordinata = True
        for i in range(n-1-num_scansioni):  # ad ogni iterazione il numero di coppie da
                                            # analizzare diminuisce di 1
                                            # confrontiamo l'elemento in posizione i e i+1
            if s*k(a[i]) > s*k(a[i+1]):
                # scambio gli elementi, non posso dire che la lista è ordinata
                a[i], a[i+1] = a[i+1], a[i]
                ordinata = False
        num_scansioni += 1

a = [4,3,1,0,2.71]
#a = ['zero', 'uno', 'due', 'tre', 'quattro']
bubble_sort(a, reverse = False) # ordinamento per lunghezze crescenti
print(a)

