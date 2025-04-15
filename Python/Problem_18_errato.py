#a=[[75],[95,64],[17,47,82],[18,35,87,10],[20,4,82,47,65],[19,1,23,75,3,34],[88,2,77,73,7,63,67],[99,65,4,28,6,16,70,92],[41,41,26,56,83,40,80,70,33],[41,48,72,33,47,32,37,16,94,29],[53,71,44,65,25,43,91,52,97,51,14],[70,11,33,28,77,73,17,78,39,68,17,57],[91,71,52,38,17,14,91,43,58,50,27,29,48],[63,66,4,68,89,53,67,30,73,16,69,87,40,31],[4,62,98,27,23,9,70,98,73,93,38,53,60,4,23]]

a=[[3],[7,4],[2,4,6],[8,5,9,3]]
"""
1. leggo la lista e prelevo un elemento alla volta
2. passo base: l'indice del primo elemento ritorna 0 e lo sommo
3. passo 2: determino quale dei due elementi è maggiore, ritorno l'indice e sommo il suo valore
4. passo i-esimo: leggo l'elemento a partire dall'indice i preso al passo precendente fino a i+1, trovo il valore maggiore e lo sommo, ritorno l'indice
"""
def passo_base(elemento):
    valore=elemento[0]
    indice=0
    return [valore,indice]

def passo_due(elemento,ritorno):
    if elemento[ritorno[1]]>elemento[ritorno[1]+1]:
        valore=elemento[ritorno[1]]
        indice=ritorno[1]
    else:
        valore=elemento[ritorno[1]+1]
        indice=ritorno[1]+1
    return [valore,indice]
somma = 0
for elemento in a:
    if len(elemento)==1:
        #print("--",elemento)
        ritorno=passo_base(elemento)
        print(somma,"+",ritorno[0],"=",somma+ritorno[0])
        somma=somma+ritorno[0]
    else:
        #print("--",elemento)
        ritorno=passo_due(elemento,ritorno)
        print(somma,"+",ritorno[0],"=",somma+ritorno[0])
        somma=somma+ritorno[0]

print(somma)
