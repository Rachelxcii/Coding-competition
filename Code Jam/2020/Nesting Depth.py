# Problem title: Nesting Depth
# Code Jam - Problem 2 (2020)
# Language: Python 3
# Big-O Notation: O(n^2)

t = int(input()) #numero de casos
for case in range(1, t+1):
    s = str(input())
    ss = ''
    zero = False
    x = 0 #lon del string que se crea
    a = 0 # nº anterior a i
    for i in s:
        
        if a <= int(i):
            zero = True
                
        if int(i) >= 0:
            l = 0 #contador de long del for para insertar el nº
            f = 0
            for j in ss:
                if j == '(':
                    f += 1
                elif j == ')':
                    f -= 1
                l += 1
                if f == int(i) and x <= l and zero == False:
                    e1 = ss[0:l:] + str(i)
                    e2 = ss[l::]
                    x = len(e1)
                    ss = e1 + e2
                elif f == a and x <= l and zero == True:
                    x = l
                    break
                
        if int(i) >= 0 and zero == True:
            e1 = ss[0:l:] + "(" * (int(i)-f) + str(i)
            x = len(e1)
            e2 = (int(i)-f) * ")" + ss[l::]
            ss = e1 + e2
            n = int(i) #ultimo numero colocado
            zero = False
            
        a = int(i)
        
    print("Case #{}: {}".format(case, ss))
