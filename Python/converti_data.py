# -*- coding: utf-8 -*-
"""
Created on Sun Jun 26 11:40:07 2022

@author: fabio
"""

def converti_data(t):
    d_giorni={1:'primo', 2:'secondo', 3:'terzo', 4:'quarto', 5:'quinto', 6:'sesto', 7:'settimo', 8:'ottavo', 9:'nono', 10:'decimo', 11:'undicesimo', 12:'dodicesimo', 13:'tredicesimo', 14:'quattordicesimo', 15:'quindicesimo', 16:'sedicesimo', 17:'diciassettesimo', 18:'diciottesimo', 19:'diciannovesimo', 20:'ventesimo', 21:'ventunesimo', 22:'ventiduesimo', 23:'ventitreesimo', 24:'ventiquattresimo', 25:'venticinquesimo', 26:'ventiseiesimo', 27:'ventisettesimo', 28:'ventottesimo', 29:'ventinovesimo', 30:'trentesimo', 31:'trentunesimo'}
    d_mese={1:'Gennaio', 2:'Febbraio', 3:'Marzo', 4:'Aprile', 5:'Maggio', 6:'Giugno', 7:'Luglio', 8:'Agosto', 9:'Settembre', 10:'Ottobre', 11:'Novembre', 12:'Dicembre'}
    
    a=[]
    
    for x in range(len(t)):
        if x==0:
            a.append(d_giorni[t[x]])
        if x==1:
            a.append(d_mese[t[x]])
        if x==2:
            a.append(t[x])
        
    a=tuple(a)
    return a
    
t = (10,3,1997)
res=converti_data(t)
print(res)