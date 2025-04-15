def palindromo(numero):
    inizio = 0
    fine = len(numero)
    test = True
    
    while (inizio<=fine):
        if(numero[inizio] == numero[fine-1]):
            inizio = inizio + 1
            fine = fine - 1
        else:
            test = False
            return test

    return test

a=100
res = 0
massimo_valore_palindromo = 0

while (a<=999):
    for b in range(900,999):
        res = a * b
        if (palindromo(str(res)) == True):
            massimo_valore_palindromo = res
    a = a + 1

print("Il valore palindromo massimo e'", massimo_valore_palindromo)
