"""
Calcolo l'equivalente decimale di un numero binario.
"""

n_binario = "10011"
n_decimale = 0
e = 0

for n in range(len(n_binario)-1,-1,-1):
    n_decimale = n_decimale + int(n_binario[n]) * 2**e
    e += 1

print("La conversione di", n_binario, "e'",n_decimale)
