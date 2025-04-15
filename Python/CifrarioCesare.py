#scrivere un programma che tramite il cifrario di cesare codifichi la stringa in input.

def CifrarioCesare(s, chiave):
    a = []
    b = ""
    for i in s:
        a.append(ord(i)+chiave)

    for i in a:
        b = b+chr(i)
        
    return b

print("Fabio =", str(CifrarioCesare('Fabio',5)))
print("Elisa =", str(CifrarioCesare('Elisa',5)))
print("Paola =", str(CifrarioCesare('Paola',5)))