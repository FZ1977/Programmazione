lato = []
numero_lati = 3

for i in range(numero_lati):
    lato.append(int(input("Inserisci lato: ")))

max = 0
indice = 0
somma = 0

for i in range(numero_lati):
    if lato[i] > max:
        max = lato[i]
        indice = i

for i in range(numero_lati):
    if i != indice:
        somma = somma + lato[i]**2

if somma**0.5 == lato[indice]:
    print("Si tratta di un triangolo rettangolo")
else:
    print("non è un triangolo rettangolo")