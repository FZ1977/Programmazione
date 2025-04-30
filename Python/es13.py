"""
Funzione per trovare radici.
"""

def find_root(x, power, epsilon):
    if x<0 and power%2 == 0:
        return None
    low = min(-1, x)
    high = max(1, x)
    ans = (high + low)/2
    while abs(ans**power - x) >= epsilon:
        if ans**power < x:
            low = ans
        else:
            high = ans
        ans = (high + low)/2
    return ans


print(find_root(16, 4, 0.00001))
