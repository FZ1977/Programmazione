#leggo un file di testo e conto il numero dei caratteri ripetuti

def ContaCaratteri(d,riga):
    for k in riga:
        if k in d:
            d[k] += 1

    return d

def InitDict():
#maiuscole 65-90
#minuscole 97-122
    d = {}
    for m in range(65,91):
        d[chr(m)]=0

    for M in range(97,123):
        d[chr(M)]=0

    return d

myFile = open("C:\\Users\\LENOVO\\Desktop\\Git\\Python\\testo.txt",'r')

riga = myFile.readlines();
d = InitDict()

for i in riga:
    d = ContaCaratteri(d,i)

for i in d.keys():
    print(i,"#"*d[i])