import math
import random
smaller = int(input("Inserisci valore min:"))
larger = int(input("Inserisci valore max:"))
maxRetry = 10
count = 0
lista = []
while count < maxRetry:
    count += 1
    computerNumber = random.randint(smaller, larger)
    print("Ho pensato a questo numero ",computerNumber)
    Guess = input("Il valore e' piu' piccolo, grande, corretto: ")
    if Guess == "piccolo":
        smaller = computerNumber
        append.lista(computerNumber)
    elif Guess == "grande":
        larger = computerNumber
        append.lista(computerNumber)
    else:
        print("Wow! ho indovinato il numero in", count, "tentativi")
        break

print("Hai mentito sul numero pensato!!!")
            
            



