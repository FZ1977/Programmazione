# -*- coding: utf-8 -*-
"""
Sia dato un numero intero positivo N inserito da tastiera. Si scriva un programma in
linguaggio PYTHON che calcoli i numeri interi che sono divisori (con resto uguale a zero) di N.
Dire inoltre se N è un numero primo.
Suggerimento.
• Un numero M è divisore di un numero N se il resto della divisione N/M è uguale a
zero.
• Un numero è primo se è divisibile solo per 1 o per il numero stesso.

@author: TL002227
"""

n = int(input("Inserisci un numero intero: "))
cnt = 0

for d in range(2,n):
    if(n%d == 0):
        print(d, "e' divisore di", n)
        cnt +=1

if(cnt > 1):
    print(n, "non e' un numero primo.")
else:
    print(n, "e' un numero primo.")