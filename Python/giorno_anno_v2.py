# -*- coding: utf-8 -*-
"""
Created on Sun Oct 15 09:26:45 2023

@author: Fabio Zangari
"""

def days(giorno, mese):
    giorniMese=[0,31,28,31,30,31,30,31,31,30,31,30,31]
    somma=0

    for i in range(1,mese):
        somma=somma+giorniMese[i]
        
    somma=somma+giorno

    return somma

def verify(giorno, mese):
    if(giorno==0):
        print("Hai inserito un giorno errato.\n")
        return 1

    if(mese>12):
        print("Hai inserito un mese sbagliato.\n")
        return 1

    if(mese==11 or mese==4 or mese==6 or mese==9):
        if(giorno>30):
            print("Hai inserito un valore errato per questo mese.\n")
            return 1

    if(mese==1 or mese==3 or mese==5 or mese==7 or mese==8 or mese==10 or mese==12):
        if(giorno>31):
            print("Hai inserito un valore errato per questo mese.\n")
            return 1

    if(mese==2):
        if(giorno>28):
            print("Hai inserito un valore errato per questo mese.\n")
            return 1

    return 0

giorno=int(input("Inserisci il giorno: "))
mese=int(input("Inserisci il mese: "))

if not(verify(giorno,mese)):
    print("Numero di giorni: ",days(giorno,mese)) 