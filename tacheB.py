from tacheA import *
import time
import os
import numpy as np
import matplotlib.pyplot as plt

def DIST_1(x, y, T):
    n = len(x)
    m = len(y)
    T[0][0] = 0

    for i in range(1, n + 1):
        T[i][0] = i * Cdel

    for j in range(1, m + 1):
        T[0][j] = j * Cins

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            T[i][j] = min(T[i - 1][j - 1] + Csub(x[i - 1], y[j - 1]), T[i][j - 1] + Cins, T[i - 1][j] + Cdel)

    return T[n][m]

def SOL_1(x, y, T1):
    n = len(x)
    m = len(y)
    i = n
    j = m
    x1 = []
    y1 = []

    while (j > 0) or (i > 0):
        # si sub
        if (j > 0) and (i > 0) and (T1[i][j] == T1[i - 1][j - 1] + Csub(x[i - 1], y[j - 1])):
            x1.append(x[i - 1])
            y1.append(y[j - 1])
            i -= 1
            j -= 1
        # si insertion
        if (j > 0) and (T1[i][j] == T1[i][j - 1] + Cins):
            x1.append('-')
            y1.append(y[j - 1])
            j -= 1
        # si supression
        if (i > 0) and (T1[i][j] == T1[i - 1][j] + Cdel):
            x1.append(x[i - 1])
            y1.append('-')
            i -= 1
    return (x1, y1)


def PROG_DYN(x, y):
    T = np.zeros((len(x)+1,len(y)+1),dtype=int)

    return (DIST_1(x, y, T),SOL_1(x,y,T))


