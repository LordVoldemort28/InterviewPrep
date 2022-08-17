"""
Notice the pattern we are trying to traverse
(0, 0), (0, 1), (0, 2), (0, 3), 
(1, 0), (1, 1), (1, 2), (1, 3), 
(2, 0), (2, 1), (2, 2), (2, 3), 
(3, 0), (3, 1), (3, 2), (3, 3), 

In zigzag traverse the indices goes like this

(0, 0)
(1, 0), (0, 1) --> odd iteration where i-- and j++
(0, 2), (1, 1), (2, 0) --> even iteration where j-- and i++
(3, 0), (2, 1), (1, 2), (0, 3)
(0, 4), (1, 3), (2, 2), (3, 1), (4, 0) and so on
"""
def zigZagTraverse(arr):
    
    result = []
    
    #First we are starting with initial top left corner indices 0, 0 which is even
    i, j = 0, 0
    even = True
    
    while True:
        
        #If the indices goes negative then calculate starting position 
        #If its odd or even    
        if i < 0 or j < 0:
            maxIdx = max(i, j)
            if maxIdx % 2 == 0:
                i = 0
                j = maxIdx
                even = True
            else:
                i = maxIdx
                j = 0
                even = False

        #Append valid value in results 
        if isValid(arr, i, j):
            result.append(arr[i][j])
            
            #Break the loop if we have reached to bottom right corner
            if i == len(arr)-1 and j == len(arr[0])-1:
                break 
        
        #Even iteration
        if even:
            i += 1
            j -= 1
        #Odd iteration
        else:
            i -= 1
            j += 1
            
    return result


def isValid(arr, i, j):
    return i in range(len(arr)) and j in range(len(arr[0]))

test_cases = {
    'test_case_1': {
        'description': 'cycle test',
        'input': [
            [1, 3, 4, 10],
            [2, 5, 9, 11],
            [6, 8, 12, 15],
            [7, 13, 14, 16]
        ],
        'output': [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16],
        'active': True
    }
}

for test_name, data in test_cases.items():

    print('Running -> {} -> {}'.format(test_name, data['description']))

    if data['active'] == False:
        print('Skipped!')
        continue

    input = data['input']
    result = zigZagTraverse(input)
    if result == data['output']:
        print('Test passed!')
    else:
        print('Test fail')
        print('Expected Output: ', end="")
        print(data['output'])
        print('Actual Output: ', end="")
        print(result)
    print()
