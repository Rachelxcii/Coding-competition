# Problem title: Parenting Partnering Returns
# Code Jam - Problem 3 (2020)
# Language: Python 3
# Big-O Notation: O(n^2)

import numpy as np
t = int(input()) #numero de casos
for case in range(1, t+1):
    n = int(input()) #nº de actividades
    matriz_horario = []
    for i in range (0, n):
        fila = [int(s) for s in input().split(" ")]
        matriz_horario.append(fila + [i+1])
    mh = np.array(matriz_horario) #matriz de horario que se pude leer.
    mh = np.sort(mh.view('i8,i8,i8'), order=['f0'], axis=0).view(np.int) # ordena la matriz por 1º

    c = 0 #cameron
    j = 0 #jamie
    horario = ''
    mh3 = 0 #nº del 3º elemento de cada fila.
    
    for i in range (0,n):
        
        if c <=mh[i,0]:
            c = mh[i,1] # se toma el minuto en el que acaba la actividad
            añadir = 'C'
        
        elif j <= mh[i,0]:
            j = mh[i,1] # se toma el minuto en el que acaba la actividad
            añadir = 'J'
                    
        else:
            horario = 'IMPOSSIBLE'
            break
        
        if mh[i,0]>(24*60) or mh[i,1]>(24*60):
            horario = 'IMPOSSIBLE'
            break
        
        if len(horario) < mh[i,2]:
            horario = horario[:len(horario):] + 'X'*(mh[i,2]-1-len(horario)) + añadir
        else:
            horario = horario[:mh[i,2]-1:] + añadir + horario[mh[i,2]:len(horario):]
       
    print("Case #{}: {}".format(case, horario))
