import math
import random
smaller = int(input("Inserisci valore min:"))
larger = int(input("Inserisci valore max:"))
computerNumber = random.randint(smaller, larger)
maxRetry = 10
count = 0
while count < maxRetry:
    count += 1
    print("Ho pensato a questo numero ",computerNumber)
    Guess = input("Il valore e' piu' piccolo, grande, corretto: ")
    if Guess == "piccolo":
        smaller = computerNumber
        computerNumber = random.randint(smaller,larger)
    elif Guess == "grande":
        larger = computerNumber
        computerNumber = random.randint(smaller,larger)
    else:
        print("Wow! ho indovinato il numero in", count, "tentativi")
            
            



