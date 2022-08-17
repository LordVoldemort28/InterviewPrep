def longestUniformSubstring(string):
    maxLength = 1
    maxCount = 1
    for idx in range(1, len(string)):
        
        if string[idx] != string[idx-1]:
            maxLength = max(maxCount, maxLength)
            maxCount = 1
        else:
            maxCount += 1

    maxLength = max(maxCount, maxLength)
    return maxLength

test_cases = {
    'test_case_1': {
        'description': 'normal',
        'input': 'aaaaabbbbbbbbbbvvv',
        'output': 10,
        'active': True
    },
    'test_case_2': {
        'description': 'short',
        'input': 'aaaaavvv',
        'output': 5,
        'active': True
    },
    'test_case_3': {
        'description': 'very short',
        'input': 'vvv',
        'output': 3,
        'active': True
    },
    'test_case_4': {
        'description': 'single char',
        'input': 'v',
        'output': 1,
        'active': True
    },
    'test_case_5': {
        'description': 'weird char',
        'input': 'ja;sdjfn;aklnsdf;lkansdg',
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
    result = longestUniformSubstring(input)
    if result == data['output']:
        print('Test passed!')
    else:
        print('Test fail')
        print('Expected Output: ', end="")
        print(data['output'])
        print('Actual Output: ', end="")
        print(result)
    print()
