# Scrivere un programma che stampi la somma dei numeri primi maggiori di 2 e minori di 1000

test = 0
sum = 0
for i in range(3,1000):
    for x in range(2,i+1):
        if i%x == 0:
            test += 1
    if test == 1:
        sum = sum + i
    test = 0
print("La somma dei numeri primi tra 3 e 1000 e'", sum)
