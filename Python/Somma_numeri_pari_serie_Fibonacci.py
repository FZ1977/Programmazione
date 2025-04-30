def fibonacci():
    x = 1
    y = 2
    res = 2
    somma = 0
    for i in range(100):
        if (res%2 == 0 and res < 4000000):
            print(res)
            somma = somma + res
        res = x + y
        x = y
        y = res

    return somma

print("somma:",fibonacci())
