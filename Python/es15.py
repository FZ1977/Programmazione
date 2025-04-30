"""
Scrivere un funzione mult che accetti in ingresso uno o due int. Se
vengono passati due argomenti stampa il loro prodotto se chiamata con
un solo argomento stampa quello.
"""

def mult(a, b=1):
    return a*b

print(mult(3))
print(mult(3,2))
