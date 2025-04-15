import random
smaller = int(input("Inserisci valore min:"))
larger = int(input("Inserisci valore max:"))
myNumber = random.randint(smaller, larger)
count = 0
while True:
    count += 1
    userNumber = int(input("Indovina il numero:"))
    if userNumber < myNumber:
        print("Troppo piccolo")
    elif userNumber > myNumber:
        print("Troppo grande")
    else:
        print("Congratulazioni! hai indovinato il numero, ci sei riuscito in", count, "prove")
        break
