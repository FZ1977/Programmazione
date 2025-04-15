# -*- coding: utf-8 -*-
"""
Si scriva un programma in python per poter analizzare una sequenza di numeri.
Dati N numeri interi letti da tastiera si vogliono calcolare e stampare su schermo diversi
risultati:
• quanti sono i numeri positivi, nulli e negativi
• quanti sono i numeri pari e dispari
• se la sequenza dei numeri inseriti è crescente, decrescente oppure né crescente né decrescente.
@author: TL002227
"""

def num_pos_neg(a):
    n = len(a)
    i = 0
    cnt_p, cnt_n, cnt_z = 0, 0, 0
    for i in range(n):
        if(int(a[i]) > 0):
            cnt_p += 1
        elif(int(a[i])<0 ):
            cnt_n += 1
        else:
            cnt_z += 1
    print(f"Numeri positivi: {cnt_p}")
    print(f"Numeri negativi: {cnt_n}")
    print(f"Numeri nulli: {cnt_z}")
            
def num_par_dis(a):
    i, cnt_p, cnt_d = 0, 0, 0
    
    for i in range(n):
        if(int(a[i])%2 == 0):
            cnt_p += 1
        else:
            cnt_d += 1
    print(f"Numeri pari: {cnt_p}")
    print(f"Numeri dispari: {cnt_d}")
    
def seq_cre_dec(a):
    i = 0
    n = len(a)
    res_c, res_d, res = 0, 0, 0
    while(i < n-1):
        if(a[i]<a[i+1]):
            res_c += 1
        elif(a[i]>a[i+1]):
            res_d += 1
        else:
            res += 1
        i+=1
    if( res_c == 0 & res_d != 0):
        print("Sequenza di numeri decrescente!")
    elif ( res_c != 0 & res_d != 0 | res != 0):
        print("Sequenza di numeri ne crescente ne decrescente!")
    else:
        print("Sequenza di numeri crescente!")

        

i = 0
n = 5
a = []

while ( i<n ):
    a.append(input("Inserisci un valore: "))
    i += 1

num_pos_neg(a)
num_par_dis(a)
seq_cre_dec(a)