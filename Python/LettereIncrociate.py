# -*- coding: utf-8 -*-
"""
Created on Fri Mar 25 20:16:15 2022

Scrivere un programma che chiede in input due 
stringhe e, se queste hanno una lettera in 
comune, mostri le due stringe una in orizzontale 
e l'altra in verticale incrociandole sulla 
lettera in comune.

@author: fabio
"""

po = input('Inserisci la praola1: ')
pv = input('Inserisci la parola2: ')

i = 0
j = 0
n = len(po)
m = len(pv)
pos_v = 0
pos_o = 0
trovato = False

while i < n and not trovato:
    j = 0
    while j < m and not trovato:
        if po[i] == pv[j]:
            pos_v = j
            pos_o = i
            trovato = True
        j += 1
    i += 1

if trovato:
	for i in range(len(po)):
		# mostro riga i
		if i != pos_o:
			print(' '*pos_v+po[i])
		else:
			print(pv)