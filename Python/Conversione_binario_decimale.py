def bin2dec(b,n):
    decimale = 0
    p = 1
    for k in range(0,n-1):
        decimale = decimale + b[k]*p
        p=p*2

    return decimale


b=[1,0,1,1,0,1,0,0]
print(bin2dec(b,8))
