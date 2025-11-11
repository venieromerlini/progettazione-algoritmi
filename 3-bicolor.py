vis = ['NC' ,'NC' ,'NC' ,'NC' ,'NC','NC']
p = [0 ,0 ,0 ,0 ,0,0]

la = [ [1,2], #0
        [3], #1
        [4,5],  #2
        [],  #3
        [], #4
        []   #5
    ]

def stampa_tree(la, nodo=0, prefisso=""):
    figli = la[nodo]
    for i, figlio in enumerate(figli):
        ultimo = (i == len(figli) - 1)
        ramo = "└── " if ultimo else "├── "
        print(prefisso + ramo + f"{figlio} ({vis[figlio]})")
        nuovo_prefisso = prefisso + ("    " if ultimo else "│   ")
        stampa_tree(la, figlio, nuovo_prefisso)


def il_padre_è_rosso():
    

def dfs(u):
    
    if (p[u] == u): # è la root
        vis[u] = 'R'  

    vis[u] = 'R'  

    for j in range (len(la[u])): # per ogni elemento della lista di adiacenza
        v = la[u][j] # prendo il nodo   
        if  vis[v] == 'NC':
            p[v] = u
            dfs(v)

for i in range (len(la)):
    dfs(i)
print(vis)
print(p)
stampa_tree (la)


