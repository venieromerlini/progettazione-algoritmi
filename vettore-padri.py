vis = [0 ,0 ,0 ,0 ,0,0]
p = [0 ,0 ,0 ,0 ,0,0]
c = 0
la = [ [1,2], #0
        [3], #1
        [4,5],  #2
        [],  #3
        [], #4
        []   #5
    ]

def dfs(u):
    if vis[u] > 0:
        return
    vis[u] = c

    for j in range (len(la[u])):
        v = la[u][j]
        print("elemento=",la[u][j], "lista ", la[u], " sto per controllare ",v, " vis=",vis)
        if  vis[v] == 0:
            p[v] = u
            dfs(v)

for i in range (len(la)):
    c = c+1
    dfs(i)
print(vis)
print(p)


