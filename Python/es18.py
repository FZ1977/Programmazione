def media(a):
    """ Scrivere una funzione che ritorna come valore
    la media di una tupla di numeri.
    """

    for i in a:
        if type(i) != int and type(i) != float:
            print('Ci sono alcuni elementi della tupla non numerici')
            return 0
    
    numero_elementi = len(a)
    media = sum(a)/numero_elementi
    return media

a=(1,2,3,4,5,6)
print("La media della tupla", a, " e'", media(a))
