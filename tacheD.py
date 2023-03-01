from tacheA import *

def mot_gaps(k):
    return ['-']*k

def align_lettre_mot(x,y):
    i=0
    for i in range(len(y)):
        if x[0]==y[i] : break
    x = mot_gaps(i)+x+mot_gaps(len(y)-i-1)

    return (x,y)

def SOL_2_REC(x,y):
    m=len(y)
    n=len(x)
    if (len(y)==0): return(x,mot_gaps(n))

    if (len(x)==0): return(mot_gaps(m),y)

    if (n==1):return align_lettre_mot(x,y)
    #if (m=1) : a verifier si il faut faire le cas m=1
    else:
        index_i= n//2
        index_j=coupure(x,y)
        (x1,y1) =SOL_2_REC(x[0:index_i],y[0:index_j])
        (x2,y2) =SOL_2_REC(x[index_i : n],y[index_j : m])
        return(x1+x2, y1+y2)

def coupure(x, y):

    n = len(x)
    m = len(y)
    d = [[], []]  #les distances
    colonne_li = [[], []]  #colonne ligne i
    for j in range(0, m + 1):
        (d[0]).append(j * Cins)
        (d[1]).append(-1)

        (colonne_li[0]).append(j)
        (colonne_li[1]).append(-1)

    for i in range(1, n // 2 + 1):
        d[1][0] = i * Cdel
        for j in range(1, m + 1):
            d[1][j] = min([d[1][j - 1] + Cins, d[0][j] + Cdel,d[0][j - 1] + Csub(x[i - 1], y[j - 1])])
        d[0] = [k for k in d[1]]  #eviter effet de bords

    for i in range(n // 2 + 1, n + 1):
        d[1][0] = i * Cdel
        for j in range(1, m + 1):
            # D(i,j)
            d[1][j] = min(d[0][j - 1] + Csub(x[i - 1], y[j - 1]),d[0][j] + Cdel,d[1][j - 1] + Cins)
            # Passage de la colonne d'origine
            if d[1][j] == d[1][j - 1] + Cins:
                colonne_li[1][j] = colonne_li[1][j - 1]
            if d[1][j] == d[0][j] + Cdel:
                colonne_li[1][j] = colonne_li[0][j]
            if d[1][j] == d[0][j - 1] + Csub(x[i - 1], y[j - 1]):
                colonne_li[1][j] = colonne_li[0][j - 1]

        d[0] = [k for k in d[1]]
        colonne_li[0] = [k for k in colonne_li[1]]

    return colonne_li[0][m]

