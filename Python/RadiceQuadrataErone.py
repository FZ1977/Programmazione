# -*- coding: utf-8 -*-
"""
Created on Fri Mar 25 17:11:35 2022
Titolo: Algoritmo babilonese

Utilizzo l'algoritmo di ERONE per calcolare la radice quadrata di un numero.

L'algoritmo esegue i seguenti passi:
1. Iniziamo con una congettura, g.
2. Se g*g è abbastanza vicino a x, ci fermiamo e diciamo che g è la risposta.
3. Altrimenti facciamo una nuova congettura calcolando la media
   di g e x/g, cioè (g + g/x)/2
4. Utilizzando il nuovo numero congetturato, che chiamiamo di nuovo g, ripetiamo
il procedimento fino a che g*g non è abbastanza vicino a g.

@author: fabio 
"""

g = 44
x = 25
err = 0.0000001
trovato = False

while not trovato:
    if (abs(x - g*g) < err):
        trovato = True
    else:
        g = (g + x/g)*0.5

print("La radice quadrata di", x, "e'", g) 