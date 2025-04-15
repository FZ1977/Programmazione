#Qualche test sull'uso del codice iterativo

x=10
for a in range(x):
    print("ciclo for esterno",a)
    for b in range(x):
        print("----ciclo for interno",b)
        x=2
