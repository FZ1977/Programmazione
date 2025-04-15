# -*- coding: utf-8 -*-
"""
Created on Wed Jun 29 21:55:38 2022

@author: fabio
"""

def funzione(abc_list, num_list):
    for char in abc_list:
        for num in num_list:
            print(char,num)
            
    return
    
funzione(['a','b','c'], [1,2,3])