#!/usr/bin/python

def tribonacci(signature, n):
    res=0
    a=0
    b=3
    while b < n:
        for num in signature[a:b]:
            res=res+num
        signature.append(res)
        res=0
        a=a+1
        b=b+1
    return signature

print tribonacci([1,1,1],10)
