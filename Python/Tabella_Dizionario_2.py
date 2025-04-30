#Dati una tabella, un nome di una colonna della tabella
#e un valore, si eliminano le righe che hanno valore diverso
#per quella colonna e si elimina la colonna, ritorna il numero
#di righe eliminate.


def elimina_righe(tabella,colonna,valore):
    conta_righe_eliminate = 0
    for riga in range(len(tabella)):
        if tabella[riga][colonna] != valore:
            conta_righe_eliminate = conta_righe_eliminate + 1
    for riga in range(len(tabella)):
        tabella[riga].pop(colonna)

    return conta_righe_eliminate

def stampa(tabella):
    print("Nome","\t","Eta'","\t","Anno")
    for i in range(len(tabella)):
        print(tabella[i].values())

tabella=[{'nome':'Fabio', 'eta':47, 'anno':1977},{'nome':'Elisa', 'eta':11, 'anno':2013},{'nome':'Paola', 'eta':46, 'anno':1978}]

stampa(tabella)
righe_cancellate = elimina_righe(tabella,"nome","Fabio")
stampa(tabella)
print("Numero di righe cancellate",righe_cancellate)
