def ShiftLeft(b,n):
    lista = list(b)
    lun = len(lista)
    appo = 0
    while n >= 0:
        appo = lista[0]
        for i in range(lun-1):
            lista[i] = lista[i+1]
        lista[lun-1] = appo
        n -= 1

    a = ""
    for i in lista:
        a = i + a

    return a
        
def ShiftRight(b,n):
    lista = list(b)
    lun = len(lista)
    appo = 0
    while n >= 0:
        appo = lista[-1]
        for i in range(lun-1,0,-1):
            lista[i] = lista[i-1]
        lista[0] = appo
        n -= 1

    a = ""
    for i in lista:
        a = i + a

    return a


n = 5
stringa_bit = "1011011"

print(f"{stringa_bit}")
print(f"rotazione a sisnistra di {n}",ShiftLeft(stringa_bit,n))
print(f"rotazione a destra di {n}",ShiftRight(stringa_bit,n))
