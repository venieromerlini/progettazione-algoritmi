
        #0  1  2  3  4
mat = [ [0, 0, 0, 1, 0], #0
        [0, 0, 0, 1, 0], #1
        [0, 0, 0, 1, 1], #2
        [0, 0, 0, 0, 0], #3
        [0, 0, 0, 1, 0]  #4
    ]
'''
print("Matrix =", mat)


for i in range(len(mat)):
    for j in range(len(mat[0])):
        print(mat[i][j])
    print("")

'''
def pozzo(u):
    for i in range(5):
        if(i != u): #se non è lo stesso stesso
            if ( 
                mat[i][u] == 1  # se da X all'iesimo c'è un arco --> ok
                and
                mat[u][i] == 0 ): # o se dall'iesimo a me non c'è un arco --> ok
                    print(u, i , mat[i][u] == 1, mat[u][i] == 0)
            else:
                return False;
    else:
        return True



def pozzoUniversale(u):
    for i in range(5):
        if pozzo(i):
            print(i)


def pozzoUniversale2(u):
    p = 0
    for i in range(1,5):
        if( mat[p][i] == 1):
            p=i
    pozzo(p)

pozzoUniversale2(0)
