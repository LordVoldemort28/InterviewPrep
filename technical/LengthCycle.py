#https://leetcode.com/discuss/interview-question/413065/goldman-sachs-cycle-in-array-trapping-rain-water
def lengthCycle(arr, startIdx):

    #Keeping track of visited index
    visitedIdx = [startIdx]
    
    #Jumping through index till index is out of range
    while startIdx < len(arr):
        
        #Jumping to next index
        startIdx = arr[startIdx]
        
        #If already came to index then return length of visited
        if startIdx in visitedIdx:
            return len(visitedIdx)-startIdx
        
        visitedIdx.append(startIdx)
        
    return -1

test_cases = {
    'test_case_1': {
        'description': 'cycle test',
        'input': [[1, 2, 0], 0],
        'output': 3,
        'active': True
    },
    'test_case_2': {
        'description': 'cycle test',
        'input': [[1, 0], 0],
        'output': 2,
        'active': True
    },
    'test_case_3': {
        'description': 'cycle test',
        'input': [[1, 2, 3, 1], 0],
        'output': 3,
        'active': True
    },
    'test_case_4': {
        'description': 'cycle test',
        'input': [[1, 2, 3, 4], 4],
        'output': -1,
        'active': True
    },
    'test_case_5': {
        'description': 'cycle test',
        'input': [[2, 3, 4, 0], 0],
        'output': -1,
        'active': True
    },
    'test_case_6': {
        'description': 'cycle test',
        'input': [[2, 3, 0], 0],
        'output': 2,
        'active': True
    },
    'test_case_7': {
        'description': 'cycle test',
        'input': [[1, 2, 3, 4], -1],
        'output': -1,
        'active': True
    },
    'test_case_8': {
        'description': 'cycle test',
        'input': [[0], 0],
        'output': 1,
        'active': True
    }
}

for test_name, data in test_cases.items():

    print('Running -> {} -> {}'.format(test_name, data['description']))

    if data['active'] == False:
        print('Skipped!')
        continue

    input = data['input']
    result = lengthCycle(input[0], input[1])
    if result == data['output']:
        print('Test passed!')
    else:
        print('Test fail')
        print('Expected Output: ', end="")
        print(data['output'])
        print('Actual Output: ', end="")
        print(result)
    print()

