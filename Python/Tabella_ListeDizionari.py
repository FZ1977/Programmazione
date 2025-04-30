#Creo una tabella con liste di dizionari
tabella = [{"Nome": "Fabio", "Anno": 1977, "Eta":46},{"Nome": "Elisa", "Anno": 2013, "Eta": 11},{"Nome": "Paola", "Anno": 1978, "Eta":46}]

def Ordina_Tabella(tabella, colonna):
    tabella.sort(key=lambda x: x[colonna], reverse=True)

def Stampa_Tabella():
    print("Nome"+"\t"+"Anno"+"\t"+"Eta'")
    for i in range(len(tabella)):
        print(tabella[i]["Nome"],"\t",tabella[i]["Anno"],"\t",tabella[i]["Eta"])


Stampa_Tabella()
Ordina_Tabella(tabella,"Nome")
Stampa_Tabella()
