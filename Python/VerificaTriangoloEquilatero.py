#inserisco tre valori numerici in input e il programma mi deve dire se si tratta di un triangolo equilatero

numero_input = 3
lato = []

for i in range(numero_input):
    lato.append(int(input("Inserisci lato: ")))


if (lato[0] != lato[1]) or (lato[0] != lato[2]) or (lato[1] != lato[2]):
    print("Non e' un triangolo equilatero.")
else:
    print("E' un triangolo equilatero")
