"""
Recursive solution
Time complexity: O(nˆ2)
Space complexity: O(1)
"""
def sunsetViewsBruteForce(buildings, direction):
    
    direction = 1 if direction == 'EAST' else -1
    end = len(buildings) if direction == 1 else -1
    start = 0 if direction == 1 else len(buildings)-1
    
    def getMaxHeight(buildings, start, end, direction, result=[]):
        
        if start == end:
            return result
        
        maxHeightIdx = start
        maxHeight = buildings[start]
        
        for idx in range(start, end, direction):
            
            if maxHeight <= buildings[idx]:
                maxHeight = buildings[idx]
                maxHeightIdx = idx
        
        return getMaxHeight(buildings, (maxHeightIdx+direction), end, direction, result+[maxHeightIdx])
    result = (getMaxHeight(buildings, start, end, direction))
    return result if direction == 1 else result[::-1]

"""
Taking an example of skyline seeing from the bottom 
or start of give direction we just have to maintain
the record of upcoming max heights
Time complexity -> O(N)
Space complexity -> O(1)
"""
def sunsetViews(buildings, direction):
    
    if not buildings:
        return []
    
    startIdx = 0 if direction == 'WEST' else len(buildings)-1
    steps = 1 if direction == 'WEST' else -1
    nHeights = len(buildings)
    
    current = startIdx
    maxHeight = buildings[current]
    result = [current]
    
    while current in range(nHeights):
        
        if maxHeight < buildings[current]:
            result.append(current)
            maxHeight = buildings[current]

        current += steps
    return result if direction == 'WEST' else result[::-1]


"""
Another solution could be using maxStack
Time complexity -> O(N)
Space complexity -> O(N)
"""

test_cases = {
    'test_case_1': {
        'description': 'east test',
        'input': {
            'buildings': [3, 5, 4, 4, 3, 1, 3, 2],
            'direction': 'EAST'
        },
        'output': [1, 3, 6, 7],
        'active': True
    },
    'test_case_2': {
        'description': 'west test',
        'input': {
            'buildings': [3, 5, 4, 4, 3, 1, 3, 2],
            'direction': 'WEST'
        },
        'output': [0, 1],
        'active': True
    }
}

for test_name, data in test_cases.items():

    print('Running -> {} -> {}'.format(test_name, data['description']))

    if data['active'] == False:
        print('Skipped!')
        continue

    input = data['input']
    result = sunsetViews(input['buildings'], input['direction'])
    if result == data['output']:
        print('Test passed!')
    else:
        print('Test fail')
        print('Expected Output: ', end="")
        print(data['output'])
        print('Actual Output: ', end="")
        print(result)
    print()
