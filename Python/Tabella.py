#creo una tabella in python
tabella = [["colonna1","riga1","riga3","riga2"],["colonna2","riga2","riga1","riga3"],["colonna3","riga3","riga1","riga2"]]

nome_colonna=input("Inserisci il nome della colonna: ")

for colonna in len(tabella):
    if tabella[colonna] == nome_colonna:
        

for riga in range(len(tabella[0])):
    for colonna in range(len(tabella)):
        if riga == 0:
            print(tabella[colonna][riga],end="\t")
        else:
            print(tabella[colonna][riga],end="\t\t")
    print("")
