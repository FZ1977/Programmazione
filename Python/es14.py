"""
Scrivere una funzione is_in che accetti in ingresso come argomenti
due stringhe e restituisca  True se una delle due stringhe compare
all'interno dell'altra, False altrimenti.
"""

def is_in(stringa1, stringa2):
    if stringa1 in stringa2 or stringa2 in stringa1:
        return True
    else:
        return False

def test_is_in():
    test=("valore","val","rocco","cocco","venti","ventilatori","azz","raw","test","test1")
    for i in range(0,9):
        print(test[i],"-", test[i+1],"->", is_in(test[i],test[i+1]))

test_is_in()
