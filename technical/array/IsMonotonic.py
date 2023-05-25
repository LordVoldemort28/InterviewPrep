def get_direction(array):
    for i in range(1, len(array)):
        if array[i] != array[i-1]:
            return i


def isMonotonic(array):

    tone_index = get_direction(array)

    if tone_index is None:
        return True

    direction = array[tone_index-1] < array[tone_index]

    for i in range(tone_index+1, len(array)):
        if array[i] == array[i-1]:
            continue
        if direction is not (array[i-1] < array[i]):
            return False
    return True


test_cases = {
    'test_case_1': {
        'input': [-1, -5, -10, -1100, -1100, -1101, -1102, -9001],
        'output': True,
        'description': 'negative',
        'active': True
    },
    'test_case_2': {
        'input': [1, 1, 2, 3, 4, 5, 5, 5, 6, 7, 8, 8, 9, 10, 11],
        'output': True,
        'description': 'positive',
        'active': True
    },
    'test_case_3': {
        'input': [1, 1, 1, 1, 1, 1, 1, 1, 1],
        'output': True,
        'description': 'neutral',
        'active': True
    },
    'test_case_4': {
        'input': [1, 1, 1, -1, 1, 1, 1, 1, 1],
        'output': False,
        'description': 'non monotonic',
        'active': True
    }
}

for test_name, data in test_cases.items():

    print('Running -> {} -> {}'.format(test_name, data['description']))

    if data['active'] == False:
      print('Skipped!')
      continue

    input = data['input']
    result = isMonotonic(input)
    if result == data['output']:
        print('Test passed!')
    else:
        print('Test fail')
        print('Expected Output: ', end="")
        print(data['output'])
        print('Actual Output: ', end="")
        print(result)
    print()
