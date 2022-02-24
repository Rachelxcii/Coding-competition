# Problem title: Sample Problem
# Kick Start - Coding Practice 2022
# Language: Python 3
# Big-O Notation: O(n)

test = int(input())
test_case = 1

while test > 0:

    bags, kids = map(int, input().split())
    candies = list(map(int, input().split()))
    
    total_candies = 0
    
    for candy in candies:
        total_candies += candy
    
    remained_candies = total_candies % kids
    
    print('Case #' + str(test_case) + ': ' + str(remained_candies))
    
    test_case += 1
    test -= 1
