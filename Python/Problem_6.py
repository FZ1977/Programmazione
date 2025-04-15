res1 = 0
res2 = 0
differenza = 0

for i in range(1,101):
    res1 = res1 + i**2
    res2 = res2 + i

print(res2**2 - res1)
