vis = [0 ,0 ,0 ,0 ,0,0]
c = 0
la = [ [1], #0
        [3], #1
        [],  #2
        [],  #3
        [5], #4
        []   #5
    ]

def dfs(u):
    if vis[u] > 0:
        return

    vis[u] = c
    
    print("visitato", u)
    for j in range (len(la[u])):
        v = la[u][j]
        print("elemento=",la[u][j], "lista ", la[u], " sto per controllare ",v, " vis=",vis)
        if  vis[v] == 0:
            dfs(v)

for i in range (len(la)):
    c = c+1
    dfs(i)
print(vis)


