# Problem title: Book Reading
# Kick Start: Round G 2019
# Language: Python 3
# Big-O Notation: O()

t = int(input()) #numero de casos
for i in range(1, t+1):
    integer = [int(s) for s in input().split(" ")] # numero de paginas
    m = [int(s) for s in input().split(" ")] # la enumeracion de las paginas que faltan
    q = [int(s) for s in input().split(" ")] # lista del numero que el lector sólo lee los multiplos
    
    n = integer[0]

    sumpag = 0
    
    for r in q:
        sumpag += (n//r)
        for p in m:
            if (p%r)==0:
                sumpag -= 1

    print ("Case #{}: {}".format(i, sumpag))
