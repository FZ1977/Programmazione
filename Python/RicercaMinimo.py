## Algoritmo di ricerca di un valore in un array di valori

def TrovaMinimoSottoseq(a, sx, dx):
    m=sx
    for(i = sx+1, i<=dx, i=i+1):
    {
        if(a[i] < a[m]):
            m=i
    }
    return m
