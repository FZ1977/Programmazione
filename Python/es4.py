n = 10
val_max_disp = 0
n_val_pari = 0
while (n>0):
    valore = int(input('Inserisci un valore  numerico intero: '))
    if valore%2 != 0:
        if valore>val_max_disp:
            val_max_disp=valore

    n=n-1

if val_max_disp!=0:
    print("Il valore massimo dispari e'", val_max_disp, ".")
else:
     print("Non ci sono valori dispari.")
