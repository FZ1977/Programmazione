def log(x, base, epsilon):
    """ Assume che x e epsilon siano int o float,
    base un int, x > 1, epsilon > 0, power >= 1
    Restituisce un float y tale che base**y
    disti da x meno di epsilon."""

    if type(x) != int and type(x) != float:
        print("Devi inserire un float o un int.")
        return 0

    if type(base) != int:
        print("Devi inserire un valore int.")
        return 0

    lower_bound = 0
    while 2**lower_bound < x:
        lower_bound += 1
    low = lower_bound - 1
    high = lower_bound + 1
    ans = (high + low)/2
    while abs(2**ans - x) >= epsilon:
        if 2**ans < x:
            low = ans
        else:
            high = ans
        ans = (high + low)/2
    return ans, x

        
ans, x = log(4, 2, 0.001)
print(ans, 'è vicino al logaritmo in base 2 di', x)

