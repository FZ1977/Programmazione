#leggo un file di testo

chiave = 3

myFile = open("C:/Users/LENOVO/Desktop/Git/Python/testo.txt","r")

a = []
s = ""

riga = myFile.readline()

while riga:
    for c in str(riga):
        print(chr(ord(c)+chiave), end="")
    riga = myFile.readline()
    print("")
