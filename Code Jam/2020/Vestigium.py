# Problem title: Vestigium
# Code Jam - Problem 1 (2020)
# Language: Python 3
# Big-O Notation: O(n)

import numpy as np

t = int(input()) #numero de casos
for case in range(1, t+1):
    n = int(input())
    matriz = []
    for i in range (0, n):
        fila = [int(s) for s in input().split(" ")]
        matriz.append(fila)
    m = np.array(matriz)
    suma = 0
    repf=set()
    repc=set()
    rf = False
    rc = False
    r = 0
    c = 0
    for i in range (0,n):
        suma += m[i,i]
        for j in range (0,n):
            if m[i,j] in repf:
                rf = True
            if m[j,i] in repc:
                rc = True
            repf.add(m[i,j])
            repc.add(m[j,i])
        if rf == True:
            r += 1
            rf = False
        if rc == True:
            c += 1
            rc = False
        repf.clear()
        repc.clear()
        
    print ("Case #{}: {} {} {}".format(case, suma, r, c))
