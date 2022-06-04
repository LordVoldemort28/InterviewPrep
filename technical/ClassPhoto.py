#Time - O(n)
#Space - O(1)
def classPhotos(redShirtHeights, blueShirtHeights):
    # Write your code here.

    if len(redShirtHeights) < 2:
        if redShirtHeights[0] == blueShirtHeights[0]:
            return False
        return True

    noOfStudent = len(redShirtHeights)
    tone = redShirtHeights[0] < blueShirtHeights[0]

    for idx in range(1, noOfStudent):

        if (redShirtHeights[idx] < blueShirtHeights[idx]) is not tone:
            return False

    return True


test_cases = {
    'test_case_1': {
        'description': 'exception test',
        'input': {
            "blue": [2, 4, 7, 5, 1],
            "red": [3, 5, 6, 8, 2]
        },
        'output': False,
        'active': True
    },
    'test_case_2': {
        'description': 'single test',
        'input': {
            "blue": [6],
            "red": [6]
        },
        'output': False,
        'active': True
    },
    'test_case_3': {
        'description': 'single test',
        'input': {
            "red": [19, 19, 21, 1, 1, 1, 1, 1],
            "blue": [20, 5, 4, 4, 4, 4, 4, 4]
        },
        'output': False,
        'active': True
    }
}

for test_name, data in test_cases.items():

    print('Running -> {} -> {}'.format(test_name, data['description']))

    if data['active'] == False:
        print('Skipped!')
        continue

    input = data['input']
    result = classPhotos(input['red'], input['blue'])
    if result == data['output']:
        print('Test passed!')
    else:
        print('Test fail')
        print('Expected Output: ', end="")
        print(data['output'])
        print('Actual Output: ', end="")
        print(result)
    print()
