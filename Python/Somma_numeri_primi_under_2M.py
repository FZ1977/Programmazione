res = 0
n = 0
for a in range(1,2000001):
    n = 0
    for b in range(1,a):
        print(a,b,n)
        if a%b == 0:
            n = n + 1
            if n > 2:
                break

    res = res + a

print(res)
        
