unita=['one','two','three','four','five','six','seven','eight','nine']
decine=['ten','eleven','twelve','thirteen','fourteen','fifteen','sixteen','seventeen','eighteen','nineteen']
lista=['twenty','thirty','forty','fifty','sixty','seventy','eighty','ninety']
cento=['hundred']
mille=['thousand']

somma=0
conta=1

for i in unita:
    print(i)
    somma = somma + len(i)
    conta=conta+1

for i in decine:
    print(i)
    somma = somma + len(i)
    conta=conta+1

for x in lista:
    print(x)
    somma = somma + len(x)
    conta=conta+1
    for z in unita:
        print(x+' '+z)
        somma = somma + len(x) + len(z)
        conta=conta+1

for x in unita:
    for y in cento:
        print(x+' '+y)
        somma = somma + len(x) + len(y)
        conta = conta + 1
        for w in unita:
            print(x+' '+y+' '+w)
            somma = somma + len(x) + len(y) + len(w)
            conta=conta+1

for x in unita:
    for y in cento:
        for w in decine:
            #if w == 'fifteen':
            print(x+' '+y+' and '+w)
            somma = somma + len(x) + len(y) + len('and') + len(w)
            conta=conta+1
           # else:
           #     print(x+' '+y+' '+w)
           #     somma = somma + len(x) + len(y) + len(w)
           #     conta=conta+1

for x in unita:
    for y in cento:
        for w in lista:
            print(x+' '+y+' '+w)
            somma = somma + len(x) + len(y) + len(w)
            conta=conta+1
            for z in unita:
                print(x+' '+y+' and '+w+'-'+z)
                somma = somma + len(x) + len(y) + len('and') + len(w)+len('-')+ len(z)
                conta=conta+1

print('one thousand')
somma = somma + len('onethousand')
print(somma,'-',conta)
        
