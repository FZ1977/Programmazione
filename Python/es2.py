data_nascita = input("Inserisci la tua data di nascita nel formato gg/mm/aaaa: ")
if data_nascita[2]!='/' and data_nascita[5]!='/' or len(data_nascita[6:])!=4:
    print('Data non inserita nel formato corretto.')
else:
    print("Sei nato nell'anno "+data_nascita[6:]+".")
