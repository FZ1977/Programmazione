#Data in input una lista di interi e stringhe, cancella dalla lista le stringhe
#e ritorna un dizionario con chiavi le stringhe cancellate.

#devo capire se la stringa contiene sia numeri sia lettere o solo lettere
#e la tratto come una stringa
#altrimenti se contiene solo valori numerici allora e' un numero

lista = [123,"ciao",456,"programma","python",7890]
len_lista = len(lista)
i = 0
d = {}

while i < len_lista:
    if type(lista[i]) == str:
        d[lista[i]]=""
        lista.pop(i)
        len_lista = len(lista)
        i = 0
    i = i + 1

print(lista,d)

