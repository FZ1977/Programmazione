a = 1
conta = 1
test = False

while (test == False ):
    test = True
    for i in range(1,21):
        if (a%i != 0):
            test = False
            break
    if(test == True):
        print(a)
    else:
        a = a + 1
        test = False
