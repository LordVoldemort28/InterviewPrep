#Two pointer approach(Following merge sort approach)
def sortedSquaredArray(array):

    sortedArray = [0 for _ in array]

    j = len(sortedArray)-1
    low, high = 0, len(array)-1

    while low <= high:
        left, right = array[low], array[high]

        if abs(left) > abs(right):
            sortedArray[j] = left**2
            low += 1
        elif abs(left) <= abs(right):
            sortedArray[j] = right**2
            high -= 1
        else:
            print("Something is wrong with input: {}, {}".format(low, high))
        j -= 1

    return sortedArray


test_cases = {
    'test_case_1': {
        'description': 'cycle test',
        'input': [1, 2, 3, 5, 6, 8, 9],
        'output': [1, 4, 9, 25, 36, 64, 81],
        'active': True
    }
}

for test_name, data in test_cases.items():

    print('Running -> {} -> {}'.format(test_name, data['description']))

    if data['active'] == False:
        print('Skipped!')
        continue

    input = data['input']
    result = sortedSquaredArray(input)
    if result == data['output']:
        print('Test passed!')
    else:
        print('Test fail')
        print('Expected Output: ', end="")
        print(data['output'])
        print('Actual Output: ', end="")
        print(result)
    print()
