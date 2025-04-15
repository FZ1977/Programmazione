d={}
for g in range(1,4):
    d[g]=d.get(g,0)+1

for g in range(1,6):
    d[g]=d.get(g,0)+1

for g in range(4,8):
    d[g]=d.get(g,0)+1

for g in range(5,11):
    d[g]=d.get(g,0)+1

MARTELLONE=[1,2,3,5,6,7,8,9,10]
TRAPANO=[1,2,3,4,5]
SEGACCIO=[4,5,6,7]
P_MARTELLONE=10
P_TRAPANO=5
P_SEGACCIO=3

totale = sum(MARTELLONE)*10+sum(TRAPANO)*5+sum(SEGACCIO)*3
minimo = 0
giorno = 0

for i in range(1,11):
    if g in MARTELLONE:
        sconto = totale - P_MARTELLONE
    elif g in SEGACCIO:
        sconto = sconto - P_SEGACCIO
    elif g in TRAPANO:
        sconto = sconto - P_TRAPANO
    sconto = sconto + 15
    if minimo > sconto:
        minimo = sconto
        giorno = g
