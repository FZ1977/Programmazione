import sys
import os

MyPath = os.path.abspath(os.getcwd())

print(MyPath)

def Funzione1():
    print("Sono nella Funzione1")
    ToAddrFile=open("c:\FileToAddr.lst","r")
    ListToAddrFile = list(ToAddrFile.read().split(" "))
    ToAddrFile.close()
    return ListToAddrFile

def Funzione2(valore1, valore2):
    print(valore1)
    print(valore2)

def ComeSiUsa():
    print("Sei entrato nella funzione ComeSiUsa")


print(len(sys.argv) - 1)
print(type(len(sys.argv)))
