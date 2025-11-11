
        
la = [ [3], 
        [3], 
        [0, 3, 4], 
        [], 
        [3]  
    ]


def pozzo(u):
    for i in range(5): # mi scorro tutti i nodi 'n'
        if i == u: # vuol dire che sto analizzando la lista del candidato e posso skippare
            continue
        for k in range (0, len(la[i])): # itero per la lungezza della lista di adiacenza, lunghezza 'm' , non è necessario includere il controllo i!=u in quanto la len di una lista vuota mi fa saltare il ciclo
            if la[i][k] == u: # controllo che ci sia il candidato pozzo universale, se lo trovo, vuol dire che il nodo ha un arco verso il pozzo
                break
        else:
            return False # se sono arrivato a fine ciclo vuol dire che non ho trovato un nodo con un arco verso il candidato
    return True # se l'algoritmo passa "liscio" vuol dire che tutti i nodi, tranne il candidato, hanno il candidato pozzo universale come nodo raggiungibile

def pozzoUniversale(u):
    for i in range(5):
        if len(la[i]) == 0: # vale la pena controllare se è un pozzo universale solamente se il nodo NON ha archi uscenti
            if pozzo(i):
                 print(i)
    
pozzoUniversale(0)