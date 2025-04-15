"""
d_a = {'k1': 'None', 'k4': 'None', 'k6': 'None'}
#d_b = {'k1': 'None', 'k2': 'None', 'k3': 'None', 'k4': 'None', 'k5': 'None', 'k6': 'None'}
d_b = {}
a = []

for i in d_a:
    for j in d_b:
        if j == i:
            a.append(j)

print(a)
"""
a=[(0,2),(1,3),(0,4),(1,5),(0,6),(0,7)]

for n in range(len(a)):
    for i in range(len(a)-1):
        if a[i][0] == 1 and a[i+1][0] == 0:
            a[i], a[i+1] = a[i+1], a[i]

print(a)