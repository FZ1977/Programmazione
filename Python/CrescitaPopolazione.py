#sviluppo di una popolazione di organismi

PopolazioneIniziale = 500
TassoDicrescita = 2
NumeroOreAumento = 6
OreTotali = 120
Ore = 0
Popolazione = PopolazioneIniziale

while Ore <= OreTotali:
    print("Numero popolazione: ",Popolazione,"dopo",Ore,"ore")
    Popolazione = Popolazione * 2
    Ore += 6
