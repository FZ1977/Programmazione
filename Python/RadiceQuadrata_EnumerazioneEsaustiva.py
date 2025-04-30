"""
Approssimazione della radice quadrata di un valore numerico.
"""

# Algoritmo enumerazione esaustiva
print("Approssimazione con formula di enumerazione esaustiva")
x = int(input("Inserisci un valore numerico:"))
guess = 0
epsilon = 0.0001

if x < 0:
    print("Valore negativo non permesso")
else:
    while abs(x - guess*guess) > epsilon:
        print(guess,"approssimazione di radice quadrata di",x)
        guess = guess + 0.1

print("Il valore approssimato della radice quadrata di",x,"e'",guess)
print("")
print("Approssimazione con formula di Erone")
# Algoritmo di Erone g = (g + g/x)/2
x = int(input("Inserisci un valore numerico:"))
guess = x
epsilon = 0.0001

if x < 0:
    print("Valore negativo non permesso")
else:
    while abs(x - guess*guess) > epsilon:
        print(guess,"approssimazione di radice quadrata di",x)
        guess = (guess + x/guess)/2

print("Il valore approssimato della radice quadrata di",x,"e'",guess)

print("")
print("Approssimazione con algoritmo di bisezione")
# Algoritmo per bisezione
x = int(input("Inserisci un valore numerico:"))
low = 0
high = x
guess = (high + low)/2
epsilon = 0.0001

if x < 0:
    print("Valore negativo non permesso")
else:
    while abs(x - guess*guess) > epsilon:
        print(guess,"approssimazione di radice quadrata di",x)
        if guess*guess < x:
            low = guess
        else:
            high = guess
        guess = (high + low)/2        
print("Il valore approssimato della radice quadrata di",x,"e'",guess)
