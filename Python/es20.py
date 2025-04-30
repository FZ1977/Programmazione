def f(L1, L2):
    """L1, L2 sono liste della stessa lunghezza
    restituisce la somma degli elementi di L1
    elevati alla potenza dell'elemento allo
    stesso indice L2"""

    if len(L1) != len(L2):
        print("Non posso eseguire la funzione")
        return 0

    res = 0
    for i in range(len(L1)):
        res = res + L1[i]**L2[i]

    return res


L1=[1,2,3]
L2=[1,2,3]

print(f(L1,L2))
