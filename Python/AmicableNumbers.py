#Amicable Numbers
d = {}
c = 0
for i in range(1,10001):
    res = 0
    for j in range(1,i):
        if(i%j == 0):
            res = res + j
    d[i] = res

for k1,v1 in d.items():
    for k2,v2 in d.items():
        if((k1 == v2 and k2 == v1) and (k1 != v1)):
            #print(k1, v1,"---",k2, v2)
            c = c + k1 #calcolo la somma dei numeri amicabili

print(c)
