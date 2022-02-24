# Problem title: H-index
# Kick start: Training (February, 2022)
# Language: Python 3
# Big-O Notation: O(n)

test = int(input())
test_case = 1

while test > 0:
    
    papers = int(input())
    citations = list(map(int, input().split()))
    
    maximum, h_index = 0, []
    
    for number in citations:
        if number > maximum:
            maximum = number
            
    count_numbers = [0]*(maximum+1)
    count, position = 0, 0
    
    for num in citations:
        
        count_numbers[num] += 1
        
        if num >= position:
            if count_numbers[position] != 0:
                count_numbers[position] -= 1
            else:
                position += 1
                   
        h_index.append(str(position))
   
    print('Case #{}: {}'.format(test_case, ' '.join(h_index))) # output[:len(output)-1]
    
    test_case += 1
    test -= 1
