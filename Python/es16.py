"""
funzione lambda con due input numerici. Se il secondo argomento è
uguale a zero deve restiruire None altrimenti stampa il risultato
della loro divisione.
"""

a=(lambda x,y: print(None) if y == 0 else print(x/y))
a(6,2)
