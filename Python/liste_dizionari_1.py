#Dati una tabella, un nome di una colonna della tabella e un valore, si eliminano le righe che hanno valore diverso
#per quella colonna e si elimina la colonna,ritorna il numero di righe eliminate

tabella=[{"nome":"Fabio", "cognome":"Zangari","eta":46},{"nome":"Fabio", "cognome":"Zangari","eta":46},{"nome":"Pippo", "cognome":"Inzaghi","eta":48},{"nome":"Andrea", "cognome":"Rossi","eta":30},{"nome":"Giuseppe", "cognome":"Verdi","eta":25}]

colonna="cognome"
valore="Inzaghi"
l=len(tabella)
conta=0
i=0

print("tabella prima della cancellazione delle righe\n",tabella)
print("")
while i<l:
    if tabella[i][colonna]!=valore:
        tabella.pop(i)
        conta+=1
        i=0
    else:
        i+=1
    l=len(tabella)
    
print("tabella dopo la cancellazione delle",conta,"righe\n", tabella)
print("")

for d in tabella:
    d.pop(colonna)


print("tabella dopo la cancellazione della colonna\n",tabella)
