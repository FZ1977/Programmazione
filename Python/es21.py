def find_last_1(s, sub):
    """s e sub sono stringhe non vuote
    Restituisce l'indice dell'ultima
    occorrenza di sub in s.
    Restituisce None se sub non è presente in s
    """

    if len(s) ==  0 or len(sub) == 0:
        print("Non posso eseguire la funzione.")

    return s.find(sub)
            
                
                
def find_last_2(s, sub):
    """s e sub sono stringhe non vuote
    Restituisce l'indice dell'ultima
    occorrenza di sub in s.
    Restituisce None se sub non è presente in s
    """

    prima_occorrenza = []
    test = 0
    
    if len(s) == 0 or len(sub) == 0:
        print("Non posso eseguire la funzione.")

    for i in range(len(s)):
            if sub[0] == s[i]:
                prima_occorrenza.append(i)

    for x in prima_occorrenza:
        for y in range(x,len(s)):
            for z in range(len(sub)):
                if sub[z] == s[y]:
                    test += 1

            pos = x


    return x
                

print(find_last_1("stringari","ri"))
print(find_last_2("stringari","ri"))
