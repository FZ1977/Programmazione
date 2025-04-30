# Verifica se un int > 2 e' primo. Se non lo e', stampa
# il più piccolo dei suoi divisori

x = int(input("Inserisci un intero maggiore di 2: "))
#smallest_divisor = None
biggest_divisor = None
for guess in range(2,x):
    if x%guess == 0:
        biggest_divisor = guess
        #smallest_divisor = guess
        #break
#if smallest_divisor != None:
#    print("Il piu' piccolo divisore di", x,"e'", smallest_divisor)
if biggest_divisor != None:
    print("Il piu' grande divisore di", x,"e'", biggest_divisor)
else:
    print(x, "e' un numero primo")
