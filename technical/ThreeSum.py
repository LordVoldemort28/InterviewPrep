def threeSum(arr, target):
    
    arr.sort()
    results = []
    
    #Iterating till second last element because we at least three items
    for idx in range(0, len(arr)-2):
        
        left = idx+1
        right = len(arr)-1
        
        while left < right:
            
            currentElements = [arr[idx], arr[left], arr[right]]
            currentSum = sum(currentElements)
            
            if currentSum == target:
                results.append(currentElements)
                #Look for another set
                left += 1
                right -= 1
            elif currentSum < target:
                left += 1
            else:
                right -= 1
                
    return results

test_cases = {
    'test_case_1': {
        'description': 'normal test',
        'input': {
            'array': [12, 3, 1, 2, -6, 5, -8, 6],
            'target': 0
        },
        'output': [[-8, 2, 6], [-8, 3, 5], [-6, 1, 5]],
        'active': True
    },
    'test_case_2': {
        'description': 'small test',
        'input': {
            'array': [1, 2, 3],
            'target': 6
        },
        'output': [[1, 2, 3]],
        'active': True
    }
}

for test_name, data in test_cases.items():

    print('Running -> {} -> {}'.format(test_name, data['description']))

    if data['active'] == False:
        print('Skipped!')
        continue

    input = data['input']
    result = threeSum(input['array'], input['target'])
    if result == data['output']:
        print('Test passed!')
    else:
        print('Test fail')
        print('Expected Output: ', end="")
        print(data['output'])
        print('Actual Output: ', end="")
        print(result)
    print()
