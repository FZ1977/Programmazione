# -*- coding: utf-8 -*-
"""
Created on Sat Dec  9 16:37:01 2023

@author: Fabio Zangari
"""

f = open("C:\\Users\\LENOVO\\Desktop\\Git\\Python\\CorsoProgrammazionePython\\CongettureBisezione.csv", "a")

for x in range(1000):
    e = 0.01
    g = 0
    low = 0
    high = max(1, x)
    ans = (high + low)/2
    
    while abs(ans*ans - x) >= e: # O(log n)
        print("low:", low, 'high:', high, 'ans:', ans)
        g += 1
        if ans*ans > x:
            high = ans
        else:
            low = ans
        ans = (high + low)/2
    s = str(x)+";"+str(g)+'\n'
    f.write(s)
    print("Numero di congetture: ", g)
    print(ans, "e' vicino alla radice quadrata di ",x)
    
f.close()
    