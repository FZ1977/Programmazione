#voglio clonare una lista utilizzando la ricorsione per evitare l'aliasing


def ricorsione(n,res=0):
    print(n)
    if n == 0:
        return res
    else:
        res=res+n
        return ricorsione(n-1,res)
        

print(ricorsione(5))
