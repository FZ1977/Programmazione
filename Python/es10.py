#Uso della ricerca per bisezione per approssimare la radice cubica sia dei
#numeri positivi sia per quelli negativi.

x=-25

if x < 0:
    low = x
else:
    low = 0
    
epsilon = 0.01
num_guesses = 0
high = max(1, x)
ans = (high + low)/2

while abs(ans**3 - x) >= epsilon:
    print("basso=", low, "alto =", high, "ans =", ans)
    num_guesses += 1
    if ans**3 < x:
        low = ans
    else:
        high = ans
    ans = (high + low)/2
print("numero di congetture = ", num_guesses)
print(ans, "e' vicino alla radice quadrata di ", x)
