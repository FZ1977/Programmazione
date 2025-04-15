# -*- coding: utf-8 -*-
"""
Created on Fri Sep 15 16:24:11 2023

@author: Fabio Zangari
"""

def triangle_number(x, max_divisor=5):
    res = 0
    for i in range(1,x+1):
        res = res + i
        """
        if len(str(res)) == 1:
            print('     ',res,':',end="")
        elif len(str(res)) == 2:
            print('    ',res,':',end="")
        elif len(str(res)) == 3:
            print('   ',res,':',end="")
        elif len(str(res)) == 4:
            print('  ',res,':',end="")
        elif len(str(res)) == 5:
            print(' ',res,':',end="")
        elif len(str(res)) == 6:
            print('',res,':',end="")
        """
        conta = 0
        for x in range(1,res+1):
            if res%x == 0:
                conta = conta + 1
                print(i, conta)
                if conta >= max_divisor:
                    print(res)
                    return True
        
triangle_number(1000000000,max_divisor=500)