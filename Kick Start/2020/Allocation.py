# Problem title: Allocation
# Kick Start: Round A 2020
# Language: Python 3
# Big-O Notation: O(n)

t = int(input()) #numero de casos
for i in range(1, t+1):
    n, b = [int(s) for s in input().split(" ")] # numero casas y saldo
    prices = [int(s) for s in input().split(" ")] # precio casas
    prices.sort()
    suma = 0
    ncasas = 0
    for p in prices:
        if (suma + p) <= b :
            suma += p
            ncasas += 1
    print ("Case #{}: {}".format(i, ncasas))
