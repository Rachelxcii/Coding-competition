# Problem title: Centauri Prime
# Kick Start - Coding Practice 2022
# Language: Python 3
# Big-O Notation: O(1)

test = int(input())
test_case = 1

vowels, consonants = 'aeiou', 'bcdfghjklmnpqrstvwxz'
vowels, consonants = set(vowels), set(consonants)

while test > 0:
    
    kingdom = str(input())
    
    if kingdom[-1].lower() in vowels:
        king = 'Alice'
    elif kingdom[-1].lower() in consonants:
        king = 'Bob'
    else:
        king = 'nobody'
    
    print('Case #{}: {} is ruled by {}.'.format(test_case, kingdom, king))
    
    test_case += 1
    test -= 1
