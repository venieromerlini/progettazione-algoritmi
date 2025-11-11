
        
la = [ [3], 
        [3], 
        [0, 3, 4], 
        [], 
        [3]  
    ]


def pozzoADJ2(G):
    n = len(G)
    arcIn = [0] * n
    arc_zero_out = []
    for i in range(n):
        arc_out_i = 0
        for vertice in G[i]:
            arcIn[vertice] += 1
            arc_out_i += 1
        if arc_out_i == 0:
           arc_zero_out.append(i)
    if len(arc_zero_out) != 1 : 
        print("no pozzo")
    candidato = arc_zero_out[0]
    if arcIn[candidato] == n-1 :
         print(candidato)
    else:
        print("no pozzo") 
    
pozzoADJ2(la)