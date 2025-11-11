vis = [0 ,0 ,0 ,0 ,0,0]
p = [0 ,0 ,0 ,0 ,0,0]
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
    vis[u] = 1
    for j in range (len(la[u])):
        v = la[u][j]
        if  vis[v] == 0:
            p[v] = u
            if(dfs(v) == True):
                return True
        else:
            return True
    else:
        return False

print(dfs(0))
print(vis)
print(p)


