def f(n):
    if n==0:
        print("--Esco dalla funzione")
        return str(n)
    else:
        for i in range(n,0,-1):
            if i>0:
                a=str(i)
                print("Richiamo la funziona")
                a=f(i-1)+a
                print(a,"Continuo ed esco")
        
print(f(10))
