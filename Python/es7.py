#Scrivere un programma che chieda all'utente di inserire un numero intero
#e stampi due numeri interi, root e pwr, tali che 1 < pwr < 6
#e root**pwr e' uguale all'intero inserito dall'utente.
#Se non esiste una coppia di interi con questa caratteristica, deve stampare
#un messaggio che lo segnali

x = int(input("Inserisci un intero: "))
test = False

if x == 1:
    print("Valore di pwr: sono tutti i numeri interi")
    print("Valore di root: 1")

for pwr in range(1,7):
    if test == False:
        for root in range(2,x):
            if x == root**pwr:
                print("Valore di pwr: ", pwr)
                print("Valore di root: ", root)
                test = True
    else:
        break

if test == False:
    print("Non ci sono valori")
