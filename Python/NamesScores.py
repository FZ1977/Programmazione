def OrdinaListaFile(file):
    #fd = open(r'C:\Users\tl002227\OneDrive - Fibercop\Develop\Python\0022_names.txt','r')
    lista = []
    fd = open(file,'r')
    contenuto = fd.read()
    elementi = contenuto.split(',')
    for i in elementi:
        lista.append(i.replace('"',''))

    return lista

def ContaNome(nome):
    alfabeto = ['','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    res = 0
    for i in nome:
        res = res + alfabeto.index(i)

    return res

l=OrdinaListaFile(r'C:\Users\tl002227\OneDrive - Fibercop\Develop\Python\0022_names.txt')
l.sort()
somma = 0

for x in l:
    somma = somma + ContaNome(x)*(l.index(x)+1)

print(somma)
