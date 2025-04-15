# -*- coding: utf-8 -*-
"""
Created on Fri Apr 19 21:24:08 2024

@author: Fabio Zangari
"""

numero_righe = int(input("Inserisci il numero di righe: "))
numero_colonne = int(input("Inserisci il numero di colonne: "))

for r in range(numero_righe):
    for c in range(numero_colonne):
        if r==0 or r==numero_righe-1:
            print("*", end='')
        elif r!=0 and r!=numero_colonne-1 and c==0 or c==numero_colonne-1:
            print("*",end='')
        else:
            print(" ",end='')
    print("")
#%% 1
numero_righe = int(input("Inserisci il numero di righe: "))
numero_colonne = int(input("Inserisci il numero di colonne: "))

for r in range(numero_righe):
    if r==0 or r==numero_righe-1:
        print(numero_colonne*"*")
    elif r!=0 and r!=numero_righe-1:
        print("*"+" "*(numero_colonne-2)+"*")
    else:
        print(" ",end='')
    
#%% 2
stringa = input("Inserisci una stringa: ")
numero_vocali = 0
for s in stringa:
    if s in "AaEeIiOoUu":
        numero_vocali = numero_vocali + 1
        
print("Il numero di vocali contenute nella stringa sono: ",numero_vocali);

#%% 3
a = input("Inserisci la stringa 1: ")
b = input("Inserisci la stringa 2: ")

pos = -1

len_a = len(a)
len_b = len(b)

for i in range(len_a - len_b + 1):
    #print(a[i:i+len_b])
    if b == a[i:i+len_b]:
        pos = i
    
print(pos)        

#%% 4
a = input("Inserisci a: ") #orizzontale
b = input("Inserisci b: ") #verticale

riga = 0
colonna = 0
trovata = False

# faccio in modo che sulla stringa orizzontale ci sia la parola piu' lunga
if len(a) < len(b):
    appo = a
    a = b
    b = a

for x in a:
    if trovata == False:
        riga = 0
    for y in b:
        if trovata == False and x == y:
            trovata = True
            break
        if trovata == False:
            riga = riga + 1
    if trovata == False:
        colonna = colonna + 1

for i in b[:riga]:
    print(" "*colonna+i)

print(a)

if riga<len(b):
    for i in b[riga+1:]:
        print(" "*colonna+i)
        
#%% 5
a = input("Inserisci la stringa a: ")
b = input("Inserisci la stringa b: ")

if len(a)<len(b):
    differenza = (len(b) - len(a))//2
    print(b)
    print(" "*differenza+a)
else:
    differenza = (len(a) - len(b))//2
    print(a)
    print(" "*differenza+b)
    
#%% 6
a = input("Inserisci una stringa: ")

flag = True
conta = 0
numero = ""

for i in a:
    if i not in "0123456789":
        flag = False
    
if flag:
    for i in a[::-1]:
        numero = i+numero
        conta = conta + 1
        if conta == 3:
            numero = "."+numero
            conta = 0
else:
    print("la stringa contiene valori non numerici.")
            
print(numero)

#%% 7
a = input("Inserisci una stringa: ")
evidenzia = ""

print(a)

for i in a:
    if i in "AaEeIiOoUu":
        evidenzia = evidenzia + "*"
    else:
        evidenzia = evidenzia + " "
        
print(evidenzia)

#%% 8
n = int(input("Inserisci un valore intero maggiore di 2: "))

max_divisore = 0
numero_primo = True

if n <= 2:
    print("Non posso continuare!!!")
else:
    if n%2 == 0:
        max_divisore = n/2
    for i in range(2,n):
        if n%i == 0:
            numero_primo = False
            max_divisore = i
    if numero_primo:
        print("n e' un numero primo.")
    else:
        print(max_divisore)
        
#%% 9
n = int(input("Inserisci un intero: "))

for pwr in range(2,6):
    root = n**(1/pwr)
    if int(root)**pwr == n:
        print("root=",int(root)," ","pwr=",pwr)
    else:
        print("Non esiste una coppia di numeri.")
        
#%% 10

#Scrivere un programma che stampi la somma dei numeri primi maggiori di 2 
#e minori di 1000. Suggerimento: probabilmente sarà il caso di usare un ciclo 
#for che sia un test di primalità, annidato all'interno di un ciclo for che 
#iteri sugli interi dispari compresi tra 3 e 999.
somma = 0

for i in range(2,1000):
    numero_pari = False
    numero_non_primo = 0
    
    if i%2 == 0 and i!=2:
        numero_pari = True
    
    for n in range(2,i):
        if i%n == 0 and n != i and numero_pari == False:
            numero_non_primo = numero_non_primo + 1
            
    if numero_non_primo == 0 and numero_pari == False:
        print(i)
        somma = somma + i
        
print(somma)

#%% 11
#approssimazione della radice cubica dei numeri negativi.

x = -25
epsilon = 0.01
num_guesses, low = 0, min(-1,x)
high = max(1, x)
ans = (high + low)/2
while abs(ans**3 - x) >= epsilon:
    print('low =', low, 'high =', high, 'ans =', ans)
    num_guesses += 1
    if ans**3 < x:
        low = ans
    else:
        high = ans
    ans = (high + low)/2

print('numero di congetture =', num_guesses)
print(ans, 'è vicino alla radice quadrata di', x)

#%% 12
#Scrivere un programma che chieda all'utente le coordinate x ed y di un punto 
#e verifichi se questo sia interno o esterno al cerchio di raggio 10 e centro 
#nell'origine degli assi. Nel primo caso stampi Interno, altrimenti stampi la 
#distanza del punto dalla circonferenza. Un punto sulla circonferenza è da 
#considerarsi interno.

def radice_quadrata(x):
    epsilon = 0.01
    num_guesses, low = 0, 0
    high = max(1, x)
    ans = (high + low)/2
    while abs(ans**2 - x) >= epsilon:
        #print('low =', low, 'high =', high, 'ans =', ans)
        num_guesses += 1
        if ans**2 < x:
            low = ans
        else:
            high = ans
        ans = (high + low)/2
    
    return ans

punto_x = int(input("Inserisci il valore x: "))
punto_y = int(input("Inserisci il valore y: "))

distanza_origine = radice_quadrata(punto_y**2 + punto_x**2)

if distanza_origine <= 10:
    print("Interno")
else:
    print(abs(distanza_origine - 10))
    
#%% 13
#Scrivere un programma che chieda all'utente di inserire una sequenza di numeri 
#e, per ogni numero inserito a partire dal terzo, stampi la media troncata 
#ovvero la media dei valori inseriti scartando il valore minimo e massimo.

min_numero = 0
max_numero = 0
conta = 0
somma = 0

while True:
    numero = float(input("Inserisci un numero: "))
    conta = conta + 1
    somma = somma + numero
    if numero > max_numero:
        max_numero = numero
    if numero < min_numero:
        min_numero = numero
    if conta >= 3:
        media = (somma - max_numero - min_numero)/(conta-2)
        print(f'La media troncata: {media}')
        
#%% 14
#Approssimazione di p-greco

def p_greco(n):
    #definisco i valori iniziali
    a0=1
    b0=1/(2**0.5)
    p0=1
    q0=1/4
    
    a,b,p,q = 0,0,0,0
    
    for i in range(n):
        a=(a0+b0)/2
        b=(a0*b0)**0.5
        p=2*p0
        q=q0-p0*(a0-a)**2
    
        a0=a
        b0=b
        p0=p
        q0=q
    
    return ((a+b)**2)/(4*q)

for n in range(1,20):
    pg=p_greco(n)
    print(f"Approssimazione di pgreco per {n} = {pg}")
    
#%% 15
#La successione di Fibonacci è composta dagli interi 0, 1, 1, 2, 3, 5, 8, 13, 
#21, 34, 55, 89, 144,... In particolare i primi due valori sono 0 e 1, ogni 
#altro valore è dato dalla somma dei due precedenti. Scrivere un programma che 
#chieda in input un numero n e stampi il valore in posizione n della successione. 
#Si tenga conto che il primo elemento della successione è in posizione 0.

def fibonacci(n):
    
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        fib_1, fib_2 = 0, 1
        while n>1:
            fib = fib_1+fib_2
            fib_1 = fib_2
            fib_2 = fib
            n = n - 1
    return fib

for n in range(10):
    valore=fibonacci(n)
    print(f'Alla posizione {n} corrisponde il valore {valore}')
    
#%% 16
#Si scriva una funzione denominata mult che accetti uno o due int. 
#Se chiamata con due argomenti, la funzione stampa il prodotto. 
#Se chiamata con un argomento, stampa quello.

def mult(*valore):
    if len(valore) == 2:
        return valore[0]*valore[1]
    else:
        return valore[0]
    
mult(3)

#%% 17

def log(x, base, epsilon):
    """
    Assume che x ed epsilon siano int o float, base un int,
        x > 1, epsilon > 0, power >= 1
    Restituisce un float y tale che base**y disti da x meno di
        epsilon
    """
    lower_bound = 0
    while base**lower_bound < x:
        lower_bound += 1
        low = lower_bound - 1
        high = lower_bound + 1
        # Ricerca per bisezione
        ans = (high + low)/2
    while abs(base**ans - x) >= epsilon:
        if base**ans < x:
            low = ans
        else:
            high = ans
        ans = (high + low)/2
    return ans

x=4
ans=log(x,2,0.01)
print(ans, 'è vicino al logaritmo in base 2 di', x)

#%% 18
#Scrivere una espressione lambda che ritorna None se il secondo parametro e' 0
#altrimenti ritorna il valore della divisione.
ans = lambda x,y: x/y if y!=0 else None
print(ans(4,2))

#%% 19
def find_last(s, sub):
    """
    s e sub sono stringhe non vuote
    Restituisce l'indice dell'ultima occorrenza di sub in s,
        None se sub non è presente in s
    """
    ans = s.find(sub)
    if ans != -1:
        return ans+len(sub)-1
    else:
        return None
    
print(find_last("rinoceronte", "noce"))

#%% 20
#valore di default della variabile key key=lambda x: -x

def find_max(a,b,c,key=lambda x: x):
    #massimo = None
    if key(a) >= key(b) and key(a) >= key(c) :
        massimo = a
    elif key(b) >= key(c):
        massimo = b
    else:
        massimo = c
    
    return massimo

print(find_max(2,16,-1,key=lambda x: -x))
print(find_max('programma', 'python', 'algoritmo'))
print(find_max('programma', 'python', 'algoritmo', key=len))

#%% 21
#Scrivere una funzione, denominata barre, che prenda in input un numero 
#variabile di interi e mostri l'input utilizzando un diagramma a barre 
#verticale come nell'esempio che segue che mostra l'output di 
#barre(3, 1, 6, 8, 0, 10, 2).

def barre(*val):
    
    lista = list(val)
    bianchi = []
    massimo = max(lista)
    numero_elementi = len(lista)
    
    for i in range(len(lista)):
        bianchi.append(massimo-lista[i])
    
    print("_"*(len(lista)+2))
    for x in range(massimo):
        print("|",end='')
        
        for i in range(numero_elementi):
            if bianchi[i] > 0:
                print(" ",end='')
                bianchi[i] = bianchi[i] - 1
            else:
                print("#",end='')
                lista[i] = lista[i] - 1
        
        print("|")
    print("-"*(len(lista)+2))    

barre(3, 1, 6, 8, 0, 10, 2)

#%% 22
#Converto maiuscole in minuscole
c = input("Inserisci un carattere maiuscolo: ")
print(chr(ord('a') + (ord(c)-ord('A'))))

#%% 23
#sort metodo per le liste sorted funzione che non modifica l'oggetto

l=[-31, 3, 9, -1, -12, 7, 22, 11]
t=(-31, 3, 9, -1, -12, 7, 22, 11)

#il metodo sort modifica la lista
print("prima di eseguire il metodo sort")
print(l)
print("primo sort")
l.sort()
print(l)
print("secondo sort")
l.sort(key=lambda k: k**2)
print(l)

print("prima di eseguire il metodo sort")
print(t)

try:
    t.sort()
    print("primo sort")
    print(t)
except:
    print("Il metodo sort non si puo applicare alle tuple")

try:
    t.sort(key=lambda k: k**2)
    print("secondo sort")
    print(t)
except:
    print("Il metodo sort non si puo applicare alle tuple")
    
#%% 24
#media di una tupla di numeri

def media(t):
    return sum(t)/len(t)

t=(1,2,3,4,5,6,7,8,9)
print(media(t))

#%% 25
#Scrivere una comprensione di lista che generi tutti i numeri non primi fra 2 e 100.
lista=[i for i in range(2,100) if (i%2==0 or i%3==0 or i%5==0 or i%7==0) and (i!=2 and i!=3 and i!=5 and i!=7)]
lista_prof=[x for x in range(2,100) if any(x%y==0 for y in range(2,int(x**0.5)+1))]
print(lista)
print(lista_prof)

#%% 26
def f(L1, L2):
    """
    L1, L2 sono liste di numeri della stessa lunghezza
    Restituisce la somma degli elementi di L1 elevati
        alla potenza dell'elemento allo stesso indice
        in L2. Per esempio, f([1,2], [2,3]) restituisce 9
    """
    if len(L1) != len(L2):
        return None
    else:
        somma = 0
        for i in range(len(L1)):
                #somma = somma + L1[i]**L2[i]
                #oppure usando la funzione lambda
                #ricorda che map legge il primo elemento di L1 e L2
                #poi esegue la funzione lambda, cosi per il secondo, il terzo e
                #il resto dei valori degli iterabili inseriti
                somma = sum(map(lambda x,y: x**y, L1, L2))
    return somma

print(f([1,2],[2,3]))

#%% 27
def get_min( d ):
    """
    d è un dict che mappa lettere su int
    restituisce il valore in d associato alla prima chiave
        in ordine alfabetico. Per esempio, se
        d = {'x': 11, 'b':12}, get_min(d) ritorna 12.
    """
    return d[min(d)]

d = {'x': 11, 'b':12} 
print(get_min(d))

#%% 28
def move_max( a ):
    '''
        Precondizione: a è una lista di numeri
        Sposta il massimo di a in fondo alla lista,
            gli altri elementi occuperanno le posizioni precedenti
    '''
    massimo = max(a)
    posizione = 0
    for i in range(len(a)):
        if a[i] == massimo:
            posizione = i
            break
    appo = a[len(a)-1]
    a[len(a)-1] = massimo
    a[posizione] = appo

a=[1,4,9,3,10,5,6,8,0,2]
print(a)
move_max(a)
print(a)

#%% 29
def move_max( a ):
    '''
        Precondizione: a è una lista di numeri
        Sposta il massimo di a in fondo alla lista,
            gli altri elementi occuperanno le posizioni precedenti
    '''
    
    temp = None
    
    for i in range(len(a)-1):
        if a[i] > a[i+1]:
            temp = a[i+1]
            a[i+1] = a[i]
            a[i] = temp

a=[1,4,9,3,10,5,6,8,0,2]
print(a)
move_max(a)
print(a)

#%% 30
# Confronto tra tuple.

#t1=("ciao","sono","una","tupla")
#t2=("programmazione","elaboratori","python","esame")

#t3=(1,2,3,5)
#t4=(1,2,4)

#print(t1>t2)
#print(t3>t4)

#True se la prima stringa e' piu' corta della seconda
#False se la seconda stringa e' piu' corta delle prima
#Se la lunghezza delle stringe e' uguale:
    #True se la prima precede la seconda lessicograficamente
    #False se la seconda precede la prima lessicograficamente
    
def confronta(s1, s2):
    if len(s1) < len(s2):
        return True
    elif len(s1) > len(s2):
        return False
    elif len(s1) == len(s2):
        if s1 < s2:
            return True
        else:
            return False

s1="programma"
s2="programmazione"        
print(confronta(s1,s2))

#%% 31
#confronto tra stringhe
def longest(a):
    massimo = ""
    for i in a:
        if len(i) > len(massimo):
            massimo = i
        if len(i) == len(massimo):
            if i > massimo:
                massimo = i
                
    return massimo

a=['stringa','righe','rinoceronte','noce','rinoceronti']
print(longest(a))

#%% 32
#Si scriva una funzione Python, denominata sort_by_len, che riceva in input 
#una lista di numeri (int o float) e la muti in modo che gli elementi siano 
#ordinati per numero di cifre crescenti.

def sort_by_len(a):
    flag = True
    while flag:
        flag = False
        for i in range(len(a)-1):
            if len(str(a[i]).replace(".","")) > len(str(a[i+1]).replace(".","")):
                a[i], a[i+1] = a[i+1], a[i]
                flag = True
            
a = [3.14, 3133, 8, 123456, 1.2345]
print(a)
sort_by_len(a)
print(a)

#%% 33
#Si scriva una funzione Python, chiamata sort_by_occurrences, che prenda una 
#stringa in input e restituisca una nuova stringa in cui i caratteri della 
#stringa originale sono ordinati dal più frequente al meno frequente.

def sort_by_occourrences(a):
    d = {}
    for i in a:
        if i not in d.keys():
            d[i]=1
        else:
            d[i]=d[i]+1
    
    stringa=""
    lista=sorted(d.values())
    print(lista)
    
    for l in lista:
        for k,v in d.items():
            if l == v:
                stringa=stringa+k
        
    return stringa

a = ')-:))-'

print(a)
print(sort_by_occourrences(a))

#%% 34
#Scrivere una funzione denominata inverti_dizionario che prenda in input un 
#dizionario d e restituisca un dizionario d_inv che abbia per chiavi i valori 
#in d e d_inv[v] sia la lista di chiavi che d mappa in v.

def d_inv(d):
    d_inv={}
    for k,v in d.items():
        if v in d_inv:
            d_inv[v] = d_inv[v] + [k]
        else:
            d_inv[v] = [k]
    return d_inv

d = { 'k0': 'v0', 'k1': 'v1', 'k2': 'v0' }
print(d)
print(d_inv(d))

#%% 35
#Scrivere una funzione denominata sort_by_type che prenda una lista che può 
#contenere int, float o str. La funzione ritorni una nuova lista in cui gli int 
#precedano i float che precedano le str. Si risolva senza utilizzare il metodo 
#sort.

def sort_by_type(a):
    lista=[]
    
    for t in int,float,str:
        for i in a:
            if type(i) == t:
                lista.append(i)
    
    return lista

a=['lista',1,3.14,3,'programmazione',2.71]
print(a)
print(sort_by_type(a))

#%% 36
#mostra la predisposizione delle torri sulla scacchiera

def show_board(posizione):
    i = 0
    for r in range(5,-1,-1):
        for c in range(0,6):
            if r == posizione[c]:
                print("#",end="")
            else:
                print("_",end="")
        print("")

a=[2, 2, 3, 1, 4, 4]
show_board(a)

#%% 37
#Si scriva una funzione, denominata check_rook_pos, che prenda in input una 
#lista come board e restituisca True se e solo le torri in board non si 
#attaccano.

def check_rook_pos(posizione):
    flag = True
    for colonna in posizione:
        if posizione.count(colonna) > 1:
            flag=None
    
    return flag
    
    
#a=[2, 2, 3, 1, 4, 4]
a=[0,1,2,3,4,5]
print(check_rook_pos(a))

#%% 38
#Si scriva una funzione che prenda in input due coppie che descrivono le 
#posizioni di due regine in una scacchiera di dimensione n x n e che 
#restituisca True se e solo se le due regine si attaccano (sono sulla stessa 
#riga, colonna o diagonale).
#Le coppie che descrivono le posizioni hanno come primo valore una lettera che 
#rappresenta la colonna (a è la prima colonna, b la seconda e così via), ed un 
#numero da 1 in poi che rappresenta la riga.

def check_rook_queen(regina1, regina2):
    scacco = None
    colonna = ['a','b','c','d','e','f']
    #scacco sulla colonna
    if regina1[0] == regina2[0]:
        scacco=True
    #scacco sulla riga
    if regina1[1] == regina2[1]:
        scacco=True
    #scacco sulla diagonale
    dy=abs(colonna.index(regina1[0])-colonna.index(regina2[0]))
    dx=abs(regina1[1]-regina2[1])
    print(f"{dx},{dy}")
    if dy == dx:
        scacco=True
    
    return scacco
    
regina1=("e",5)
regina2=("b",2)
print(check_rook_queen(regina1,regina2))

#%% 39
#La somma armonica di un intero, n > 0, si può calcolare con la formula
#1 + 1/2 + 1/3 + ... + 1/n
#Scrivete una funzione ricorsiva che la calcoli.

def somma_armonica(n):
    if n == 1:
        return 1
    else:
        return 1/n + somma_armonica(n-1)
        
print(somma_armonica(5))

#%% 40
def deep_count(t):
    """
        Precondizione: t è una tupla che può contenere al suo interno tuple 
        annidate restituisce il numero di elementi numerici contenuti in t
        ed in tutte le tuple annidate.
    """
    conta = 0
    for e in t:
        if type(e) == tuple:
            conta += deep_count(e)
        else:
            conta += 1
            
    return conta


t = ( 3.14, (2, 3), (2.71, (7, 5)), 9, (12, ( 4, )) )
print(deep_count(t))

#%% 41
"""
Scrivere una funzione Python denominata deep_copy che cloni la lista in 
input e tutte le liste annidate che essa contiene.
"""

def deep_copy(a):
    l=[]
    for e in a:
        if type(e) == list:
            l.append(deep_copy(e))
        else:
            l.append(e)
            
    return l


a = [3.14, [2, 3], [2.71, [7, 5]], 9,  [12, [ 4, ]]]
print(id(a),"-",a)
l=deep_copy(a)
print(id(l),"-",l)

#%% 41
#Scrivere una funzione che stampi tutte le permutazioni di una lista in input.

def permutazioni(a):
    for i in a:
        for j in a:
            for k in a:
                if i!=j and i!=k and j!=k:
                    print(i,j,k)

def permuta( a, i  = 0):
    if i < len(a):
        for j in range(i, len(a)):
            a[i], a[j] = a[j], a[i]
            permuta(a, i+1)
            a[i], a[j] = a[j], a[i]
    else:
        print(a)
                
a=[1,2,3]
permutazioni(a)
permuta(a)

#%% 42
#test variabili globali
def f(a):
    print(a)
    global n
    n=10

n=4    
print(n)
f(n)
print(n)

#%% 43
# Sia a una lista di n interi maggiori o uguali a 0, si scriva una funzione, 
#denominata combinazioni che stampi tutte le liste b di interi maggiori o 
#uguali a zero e di lunghezza n tali che b[i] < a[i] per ogni i = 0,..., n-1.

def combinazioni(a):
    def combina(a,b,i=0):
        if i == len(a):
            print(b)
        else:
            for x in range(a[i]):
                b[i] = x
                combina(a,b,i+1)
                
    
    b=[0]*len(a)
    combina(a,b)    

a=[1,2,3]
   
combinazioni(a)

#%% 44
#Test ricorsione

def f(a,flag=True):
    if flag:
        print(f"stampo a={a} e perche' flag={flag}")
    else:
        print(f"non stampo a perche' flag={flag}")
        
a=[1,2]
f(a,flag=False)

#%% 45
#Creare una funzione ricorsiva per calcolare una funzione definita cosi:
#per m>0 allora f(n,m)=1+f(n,m-1)
#per m=0 allora f(n,m)=n

def f(n,m):
    if m>0:
        return 1+f(n,m-1)
    if m==0:
        return n
    
print(f(4,5))

#%% 46
#Creare una funzione ricorsiva che ricevuto un numero restituisce la somma 
#delle cifre del numero se questa e' minore di 10 o il risultato della 
#ri-applicazione della funzione sulla somma delle cifre del numero altrimenti.

def f(n):
    somma = 0
    for i in str(n):
        somma = somma + int(i)
        
    if somma < 10:
        print(somma)
    else:
        f(somma)
    
n=392
f(n)

#%% 47
#Scrivere il codice di una funzione ricorsiva f(n) che restituisce 0 nel caso n 
#sia dispari o zero, 1+f(n/2) altrimenti.

def f(n):
    if n%2 != 0:
        return 0
    elif n == 0:
        return 0
    else:
        return 1+f(n/2)
    
print(f(12))

#%% 48
#Scrivere il codice di una funzione ricorsiva f(n) che restituisce:
#-n nel caso n sia minore di 10
#-il risultato di f applicata alla somma delle cifre di n se n è pari
#-f(n-1) altrimenti.

def f(n):
    if n<10:
        return n
    elif n%2==0:
        somma = 0
        for x in str(n):
            somma = somma + int(x)
        return f(somma)
    else:
        return f(n-1)
    
print(f(12))

#%% 49
#Scrivere il codice di una funzione ricorsiva int f(int n) che restituisce 
#quante coppie di cifre uguali in posizioni adiacenti ci sono nel numero n, 
#nel caso n sia negativo restituisce 0.
#Ad es: f(551122) restituisce 3, f(5122) restituisce 1, f(9) restituisce 0, 
#f(444) restituisce 2.

def f(n, i=0,c=0):
    if i<len(str(n))-1:
        if str(n)[i] == str(n)[i+1]:
            f(n,i+1,c+1)
        else:
            f(n,i+1,c)
        
        if len(str(n)) == 0:
            print(0)
    else:
        print(c)
            
f(551122) #restituisce 3, 
f(5122) #restituisce 1, 
f(9) #restituisce 0, 
f(444) #restituisce 2.

#%% 50
#Scrivere una funzione ricorsiva per calcolare l’ennesimo numero della serie 
#di Fibonacci.
#La serie di Fibonacci è una serie numerica in cui il numero ennesimo è dato 
#dalla somma dei due numeri di Fibonacci che la precedono; i primi due numeri 
#di Fibonacci sono 0 e 1.

def fibonacci(n):
    if n>1:
        return fibonacci(n-1)+fibonacci(n-2)
    if n == 0:
        return 0
    if n == 1:
        return 1
        
fibonacci(6)

#%% 51
def sum_digits(s):
    """
    Assume che s sia una stringa
    Restituisce la somma delle cifre decimali in s
    Per esempio, se s è 'a2b3c', restituisce 5
    """
    i = 0
    somma = 0
    while i < len(s):
        try:
            somma = somma + int(s[i])
            i += 1
        except ValueError:
            i += 1
    
    return somma

print(sum_digits('a2b3c'))

#%% 52
def find_even( L ):
    """
    Assume che L sia una lista di interi
    Restituisce il primo numero pari in L
    Solleva ValueError se L non contiene numeri pari
    """
    primo_numero = False
    n = None
    for x in L:
        if x%2 != 0:
            raise ValueError
        if x%2 == 0 and not primo_numero:
            primo_numero = True
            n = x
    return n

L = [2,4,6,8,9]
print(find_even(L))

#%% 53
def insert_num():
    """
    Si scriva un programma che chieda all'utente di digitare 10 numeri 
    da tastiera e li inserisca in una lista. Al termine stampi la lista. 
    Si utilizzi il meccanismo di controllo delle eccezioni per assicurarsi 
    che nella lista finale vengano inseriti soltanto valori numerici.
    """
    L=[]
    for i in range(10):
        try:
            n = int(input("Inserisci un numero: "))
            L.append(n)
        except ValueError:
            pass
        
    return L

L=insert_num()
print(L)

#%% 54
def f(L):
    """
    Si scriva una funzione che prenda in input una lista contenente numeri o 
    stringhe. Restituisca la somma di tutti i numeri nella lista meno la somma 
    di tutte le lunghezze delle stringhe nella lista. Ad esempio se la lista 
    fosse [4, 'python', '3.5', 'int'], la funzione restituirebbe 
    4 - 6 + 3.5 - 3 = -1.5.
    """
    somma = 0
    for i in L:
        try:
            somma = somma + i
        except TypeError:
            somma = somma - len(i)
            
    return somma

L = [4, 'python', '3.5', 'int']
print(f(L))

#%% 55
def int_to_str(i):
    
