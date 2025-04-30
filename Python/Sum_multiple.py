def multiple(l):
    sum=0
    for i in l:
        if(i%3 == 0 or i%5 == 0):
            sum=sum+i

    return sum

l=[x for x in range(1000)]
print(multiple(l))
