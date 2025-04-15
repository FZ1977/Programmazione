#DecimalToOctal

valore = 120

a = ""

while valore > 0:
    result = valore // 8
    carry = valore % 8
    a = str(carry) + a
    valore = result


print(a)