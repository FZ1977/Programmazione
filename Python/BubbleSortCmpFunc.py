# -*- coding: utf-8 -*-
"""
Created on Sat Mar 26 20:28:13 2022

pre: a è una lista ;
cmp_func restituisce l'esito del confronto tra due elementi di a ovvero
restituisce True se e solo se il primo precede il secondo
ordina la lista dall'elemento più piccolo a quello più grande

@author: fabio
"""

def cmp_len( x, y):
    # restituisce l'esito del confronto tra le lunghezze degli argomenti
    return len(x) <= len(y)

def cmp_val( x, y):
     # restituisce l'esito del confronto tra i valori dei argomenti
    return x <= y

def cmp_val_strlen(x, y):
    '''
    pre: i tipi di x ed y sono numeri o stringhe
    restituisce l'esito del confronto tra x e y
    '''
    if type(x) in (float, int) and type(y) in (int, float):
        return x <= y
    if type(x) == str and type(y) == str:
        return len(x) <= len(y)
    # x ed y hanno tipi divesi
    if type(x) in (int, float): # allora y è str 
        return True
    else: # x non intero allora x è str allora y è numero
        return False


def bubble_sort( a, cmp_func = cmp_val_strlen ):
    n = len(a)
    ordinata = False
    num_scansioni = 0 # numero di scansioni (esecuzioni for) già eseguite
    while not ordinata:
        ordinata = True
        for i in range(n-1-num_scansioni):
            # confrontiamo l'elemento in posizione i e i+1
            if not cmp_func(a[i], a[i+1]) :
                # scambio gli elementi, non posso dire che la lista è ordinata
                a[i], a[i+1] = a[i+1], a[i]
                ordinata = False
        num_scansioni += 1
        
a = [6, 'zero', 'novantanove', 2, 'tre', 0, 'uno', 3.14]
bubble_sort(a)
print(a)