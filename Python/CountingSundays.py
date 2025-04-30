### Counting Sundays

#calcolo i giorni bisestili
def AnnoBisestile(anno):
    val = 0
    if(anno%100 != 0 and anno%4 == 0):
        val = 1
    if(anno%100 == 0 and anno%400 == 0):
        val = 1
    return val

Normale = {"Gen":31, "Feb":28, "Mar":31, "Apr":30, "Mag":31, "Giu":30, "Lug":31, "Ago":31, "Set":30, "Ott":31, "Nov":30, "Dic":31}
Bisestile = {"Gen":31, "Feb":29, "Mar":31, "Apr":30, "Mag":31, "Giu":30, "Lug":31, "Ago":31, "Set":30, "Ott":31, "Nov":30, "Dic":31}
GiorniSettimana = ["Lun","Mar","Mer","Gio","Ven","Sab","Dom"]

if(AnnoBisestile(1900) == 0):
    g = 0
    for i in Normale.keys():
        #print("------",i)
        for m in range(1,Normale[i]+1):
            #print(m," ",GiorniSettimana[g])
            g += 1
            if(g == 7):
                g = 0
else:
    for i in Bisestile.keys():
        #print("------",i)
        for m in range(1,Bisestile[i]+1):
            #print(m," ",GiorniSettimana[g])
            g += 1
            if(g == 7):
                g = 0

### Conto il numero di domeniche che cadono il primo del mese.
conta = 0
g = 1
for x in range(1901,2001):
    print("Anno",x)
    if(AnnoBisestile(x) == 0):
        for i in Normale.keys():
            for m in range(1,Normale[i]+1):
                #print(x,"-",i,"-",m," ",GiorniSettimana[g])
                if(GiorniSettimana[g] == "Dom" and m == 1):
                    #print(i,GiorniSettimana[g],"-",m)
                    conta += 1
                g += 1
                if(g == 7):
                    g = 0
    else:
        for i in Bisestile.keys():
            for m in range(1,Bisestile[i]+1):
                #print(x,"-",i,"-",m," ",GiorniSettimana[g])
                if(GiorniSettimana[g] == "Dom" and m == 1):
                    #print(m," ",GiorniSettimana[g])
                    conta += 1
                g += 1
                if(g == 7):
                    g = 0

print(conta)
