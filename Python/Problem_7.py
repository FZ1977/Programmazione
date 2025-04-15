numero_primo = 0
for i in range(1,3000000):
    conta = 0
    for x in range(1,i+1):
        if (i%x == 0):
            conta = conta + 1
    if (conta == 2):
        numero_primo = numero_primo + 1
        if ( numero_primo == 10001):
            print(i,"e' un numero primo")
            break
