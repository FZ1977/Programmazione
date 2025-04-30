#Scrivete un programma che stampi la somma dei numeri primi
#maggiori di 2 e minori di 1000.

test = 0
sum = 0

for x in range(3,1000):
    for n in range(1,x+1):
        if x%n == 0:
            test = test + 1
    if test == 2:
        print(x)
        sum = sum + x
    test = 0

print(sum)
