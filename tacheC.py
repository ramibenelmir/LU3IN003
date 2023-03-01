from tacheA import *

def DIST_2(x, y, T):
    n = len(x)
    m = len(y)
    T[0][0] = 0
    for j in range(1, m + 1):
        T[0][j] = j * Cins

    for i in range(1, n + 1):
        T[1][0] = i * Cdel
        for j in range(1, m + 1):
            T[1][j] = min(T[0][j - 1] + Csub(x[i - 1], y[j - 1]), T[1][j - 1] + Cins, T[0][j] + Cdel)
        for j in range(m + 1):
            T[0][j] = T[1][j]

    return T[1][m]



