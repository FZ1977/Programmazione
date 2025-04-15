#OctalToDecimal


Ottale = input("Inserisci un numero ottale:")

if '8' in Ottale or '9' in Ottale:
    print("Non e' un valore ottale.")
    exit
else:
    num = 0
    i = 0
    b = Ottale[::-1]
    for n in b:
        num += int(n)*(8**i)
        i += 1

    print(num)