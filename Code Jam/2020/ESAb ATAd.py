# Problem title: Parenting Partnering Returns
# Code Jam - Problem 3 (2020)
# Language: Python 3
# Big-O Notation: O(n)

import sys

t, b = [int(s) for s in input().split(" ")] #numero de casos

for case in range(1, t+1):
    
    bits = ''
    
    for i in range(1,b+1):
        print(i)
        sys.stdout.flush()
        bits += input()
    
    print(bits)
    sys.stdout.flush()
    r = input()
    
