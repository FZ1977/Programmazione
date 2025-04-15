#calcolo distanza totale percorsa dalla palla.

altezza_iniziale = int(input("Inserisci altezza: "))
numero_rimbalzi = int(input("Inserisci numero rimbalzi: "))
indice_rimbalzo = 0.6
altezza_rimbalzo = altezza_iniziale * indice_rimbalzo

distanza = 0
i = 0

while i < numero_rimbalzi:
    print("distanza:",distanza,"altezza:",altezza_iniziale,"altezza_rimbalzo:",altezza_rimbalzo)
    distanza += (altezza_iniziale + altezza_rimbalzo)
    altezza_iniziale = altezza_rimbalzo
    altezza_rimbalzo = altezza_iniziale * indice_rimbalzo
    i += 1
    
print("La distanza totale percorsa dalla palla e'", distanza);
