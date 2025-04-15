# -*- coding: utf-8 -*-
"""
Created on Wed Jun 29 07:57:00 2022

@author: fabio
"""


a = ['banana', 'pie', 'Washington', 'book']
lista=list(map(lambda x: x[::-1], a)) #map modifica la lista
#print(lista)

list(filter(lambda x: x[::-1], a)) #filter esegue controlli sulla lista