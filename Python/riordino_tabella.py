''' 
    Un modo comune di memorizzare tabelle e' come liste di dizionari. 
    Ogni riga della tabella corrisponde ad un dizionario le cui chiavi sono i nomi delle colonne della tabella.
    Questa collezione di dizionari e' poi memorizzata in una lista.
    Ad esempio la tabella
    
    nome  | anno | tel
  --------|------|---------
   Sofia  | 1973 | 5553546 
   Bruno  | 1981 | 5558432

puo' essere memorizzata come 
[{'nome': 'Sofia', 'anno': 1973 ,'tel': 5553546},{'nome': 'Bruno', 'anno': 1981 ,'tel': 5558432}]

'''


def es26(tabella, colonna):
    ''' 
    Si implementi la funzione es26(tabella,colonna) che presi in input
    - una tabella rappresentata tramite lista di dizionari
    - una stringa con il nome di una delle colonne della tabella
    modifica distruttivamente la tabella riordinandone le righe in ordine decrescente rispetto 
    ai valori contenuti nella  colonna indicata. La funzione deve restituire il numero di colonne della tabella.
        Ad esempio con  tabella = [{'nome': 'Bruno', 'anno': 1981 ,'tel': 5558432},
                        {'nome': 'Sofia', 'anno': 1973 ,'tel': 5553546}]
    al termine di es26(dati, 'anno')  la  tabella sara' stata modificata in 
    [{'nome': 'Bruno', 'anno': 1981 ,'tel': 5558432},{'nome': 'Sofia', 'anno': 1973 ,'tel': 5553546}]
    e restituisce il numero di colonne 3.
    '''
    # inserisci qui il tuo codice
    lista_chiavi=list(tabella[0].keys())
    lista=[]
    ld_appo=[]
    numero_colonne=len(tabella[0].keys())
    for elemento in tabella:
        lista=lista+[elemento[colonna]]
        lista.sort(reverse=True)

    for x in lista:
        for t in tabella:
            if t[colonna] == x:
                ld_appo=ld_appo+[t]
                

    tabella=ld_appo.copy()
    return numero_colonne, tabella

tabella=[{'nome': 'Elisa', 'anno': 2013 ,'tel': 4353546},{'nome': 'Paola', 'anno': 1978 ,'tel': 5163546},{'nome': 'Fabio', 'anno': 1977 ,'tel': 5553226},{'nome': 'Sofia', 'anno': 1973 ,'tel': 5553546},{'nome': 'Bruno', 'anno': 1981 ,'tel': 5558432}]

print("dizionario prima- ",tabella)
print("dizionario dopo - ",es26(tabella,'anno'))
