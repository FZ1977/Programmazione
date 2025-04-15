x, y, z = 1, 2, 3

if x%2 != 0 and y%2 != 0 and z%2 != 0:
    print(max(x,y,z))
if x%2 != 0 and y%2 != 0 and z%2 == 0:
    print(max(x,y))
if x%2 != 0 and y%2 == 0 and z%2 != 0:
    print(max(x,z))
if x%2 == 0 and y%2 != 0 and z%2 != 0:
    print(max(y,z))
if x%2 != 0 and y%2 == 0 and z%2 == 0:
    print(x)
if x%2 == 0 and y%2 != 0 and z%2 == 0:
    print(y)
if x%2 == 0 and y%2 == 0 and z%2 != 0:
    print(z)
if x%2 == 0 and y%2 == 0 and z%2 == 0:
    print(min(x,y,z))
