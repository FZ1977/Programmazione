# -*- coding: utf-8 -*-
"""
Created on Tue Jun 21 18:05:59 2022

Data una stringa conta:
- quante sono le vocali
- quante sono le consonanti
- quanti sono i numeri
- quanti sono il resto dei caratteri
- quante volte si ripetono i singoli caratteri

@author: fabio
"""

def conta_vocali(a):
    conta = 0
    for x in a:
        if (x == 'A' or x == 'E' or x == 'I' or x == 'O' or x == 'U' or x == 'a' or x == 'e' or x == 'i' or x == 'o' or x == 'u'):
            conta += 1
    
    return conta

def conta_consonanti(a):
    conta = 0
    for x in a:
        if ((x>='A' and x<='Z') or (x>='a' and x<='z') and (x != 'A' or x != 'E' or x != 'I' or x != 'O' or x != 'U' or x != 'a' or x != 'e' or x != 'i' or x != 'o' or x != 'u')):
            conta += 1
    
    return conta

def conta_numeri(a):
    conta = 0
    for x in a:
        if (x>='0' and x<='9'):
            conta += 1
    
    return conta

def conta_speciali(a):
    conta = 0
    for x in a:
        if ((x>='0' and x<='9') or (x>='A' and x<='Z') or (x>='a' and x<='z') and (x != 'A' or x != 'E' or x != 'I' or x != 'O' or x != 'U' or x != 'a' or x != 'e' or x != 'i' or x != 'o' or x != 'u')):
            conta += 1
    
    return conta

def conta_occorrenze(a):
    d = {}
    for x in a:
        if x not in d:
            d[x] = 1
        else:
            d[x] += 1

    v_max = max(d.values())            

    while(v_max>0):    
        for k, v in d.items():
            if d[k] == v_max:
                print(k, v, end=' ')
        v_max = v_max - 1


a = "Questa e' una stringa di test 1. conta vocali, 2. conta consonanti, 3. conta numeri, 4. conta altri caratteri, 5. ordina per numero di occorrenze, (programmazione dei calcolatori)."
print('Lunghezza della stringa: ', len(a))
print('Numero di vocali: ', conta_vocali(a))
print('Numero di consonanti: ', conta_consonanti(a))
print('Numero di numeri: ', conta_numeri(a))
print('Numero di caratteri speciali: ', conta_speciali(a))
conta_occorrenze(a)