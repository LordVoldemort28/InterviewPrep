from collections import Counter

def runLengthEncoding(string):
    encode = ''

    char, count = (string[0], 1)
    for idx in range(1, len(string)):
        if string[idx-1] != string[idx] or count == 10:
            encode += char + str(count)
            char, count = (string[idx], 1)
        else:
            count += 1
    encode += char + str(count)
    return encode
    
test_cases = {
    'test_case_1': {
        'description': 'normal test',
        'input': "AAAAABBBBBSSSSSS",
        'output': "A5B5S6",
        'active': True
    },
    'test_case_2': {
        'description': 'normal test',
        'input': "AAAAA",
        'output': "A5",
        'active': True
    },
    'test_case_3': {
        'description': 'normal test',
        'input': "A",
        'output': "A1",
        'active': True
    },
    'test_case_4': {
        'description': 'normal test',
        'input': "ssssssssssssssssssssssssssssssssssss",
        'output': "s10s10s10s6",
        'active': True
    }
}

for test_name, data in test_cases.items():

    print('Running -> {} -> {}'.format(test_name, data['description']))

        print('Skipped!')
    if data['active'] == False:
        continue

    input = data['input']
    result = runLengthEncoding(input)
    if result == data['output']:
        print('Test passed!')
    else:
        print('Test fail')
        print('Expected Output: ', end="")
        print(data['output'])
        print('Actual Output: ', end="")
        print(result)
    print()
