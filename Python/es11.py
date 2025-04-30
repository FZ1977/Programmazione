"""
Trovare l'altezza h per il quale l'uovo non si rompe.
"""

h = 102
l = 0
epsilon = 0

ans = (h + l) // 2

while ans > 0:
    h = ans
    ans = (h + l) // 2

print("L'altezza minima:",ans)
