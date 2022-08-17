def tandemBicycle(redShirtSpeeds, blueShirtSpeeds, fastest):
    
    if fastest:
        redShirtSpeeds.sort()
    else:
        redShirtSpeeds.sort(reverse=True)
        
    blueShirtSpeeds.sort(reverse=True)
    total = 0
    
    for red, blue in zip(redShirtSpeeds, blueShirtSpeeds):

        total += max(red, blue)
        
    return total

test_cases = {
    'test_case_1': {
        'description': 'fastest test',
        'input': {
            'red': [5, 5, 3, 9, 2],
            'blue': [3, 6, 7, 2, 1],
            'fastest': True
            },
        'output': 32,
        'active': True
    },
    'test_case_2': {
        'description': 'slowest test',
        'input': {
            'red': [5, 5, 3, 9, 2],
            'blue': [3, 6, 7, 2, 1],
            'fastest': False
        },
        'output': 25,
        'active': True
    },
    'test_case_3': {
        'description': 'slowest test',
        'input': {
            'red': [1, 2, 3, 4, 5],
            'blue': [5, 4, 3, 2, 1],
            'fastest': False
        },
        'output': 15,
        'active': True
    }
}

for test_name, data in test_cases.items():

    print('Running -> {} -> {}'.format(test_name, data['description']))

    if data['active'] == False:
        print('Skipped!')
        continue

    input = data['input']
    result = tandemBicycle(input['red'], input['blue'], input['fastest'])
    if result == data['output']:
        print('Test passed!')
    else:
        print('Test fail')
        print('Expected Output: ', end="")
        print(data['output'])
        print('Actual Output: ', end="")
        print(result)
    print()
