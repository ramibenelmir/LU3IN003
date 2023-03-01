from math import inf
import time
import timeit
from tools import *
import os
import matplotlib.pyplot as plt
from math import inf
import time
Cdel = 2
Cins = 2


def Csub(x,y):

    if x==y: return 0
    if ((x == 'A' and y == 'T') or (x == 'T' and y == 'A')) or ((x == 'G' and y == 'C') or (x == 'C' and y == 'G')): #partie concordante
         return 3
    return 4

def DIST_NAIF_REC(x,y,i,j,c,dist):

    if (i == len(x)) and (j==len(y)):
        if (c<dist): dist=c
    else:
        if (i < len(x)) and (j < len(y)):  dist = DIST_NAIF_REC(x,y,i+1,j+1,c+Csub(x[i],y[j]),dist)
        if (i<len(x)) : dist = DIST_NAIF_REC(x,y,i+1,j,c+Cdel,dist)
        if (j < len(y)): dist = DIST_NAIF_REC(x, y, i, j + 1, c + Cins, dist)
    return dist


def DIST_NAIF(x,y):
    return DIST_NAIF_REC(x,y,0,0,0,inf)






