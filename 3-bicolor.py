

def stampa_tree(la, nodo=0, prefisso=""):
    figli = la[nodo]
    for i, figlio in enumerate(figli):
        ultimo = (i == len(figli) - 1)
        ramo = "└── " if ultimo else "├── "
        print(prefisso + ramo + f"{figlio} ({vis[figlio]})")
        nuovo_prefisso = prefisso + ("    " if ultimo else "│   ")
        stampa_tree(la, figlio, nuovo_prefisso)

vis = ['NC' ,'NC' ,'NC' ,'NC' ,'NC','NC']
p = [0 ,0 ,0 ,0 ,0, 0]

la = [ [1,2], #0
        [3], #1
        [4,5],  #2
        [],  #3
        [], #4
        []   #5
    ]

def il_padre_è_rosso(u):
    return vis[p[u]] == 'R'
    

def dfs(u):
    if (p[u] == u): # è la root la assegno per default a Rosso
        vis[u] = 'R'  
    elif il_padre_è_rosso(u):
        vis[u] = 'N'  
    else:
        vis[u] = 'R'  

    for j in range (len(la[u])): # per ogni elemento della lista di adiacenza
        v = la[u][j] # prendo il nodo   
        if  vis[v] == 'NC': # se non colorato procedo alla dfs
            p[v] = u
            if not dfs(v): # se una delle iterazioni mi ha restituito false, interrompo e ritorno false
                return False
        elif ( vis[v] == 'R' and vis[u] == 'R' ) or (vis[v] == 'N' and vis[u] == 'N'): 
            print ("{} e {} sono dello stesso colore".format(v, u))
            return False
    else:
        return True #se finisce il ciclo vuol dire che ho iterato tutto l'albero



#for i in range (len(la)):
print(dfs(0))

print(p)
print(vis)

print("0 ({})".format(vis[0]))
stampa_tree (la)

