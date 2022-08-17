def longestPeak(arr):
    # Write your code here.
    if len(arr) < 3:
        return 0

    maxPeak = 0

    for i in range(len(arr)):

        left, leftCount = i-1, 0
        while left in range(0, len(arr)) and arr[left+1] > arr[left]:
            leftCount += 1
            left -= 1

        right, rightCount = i+1, 0
        while right in range(0, len(arr)) and arr[right-1] > arr[right]:
            rightCount += 1
            right += 1
            
        if leftCount == 0 or rightCount == 0:
            continue

        maxPeak = max((leftCount+rightCount)+1, maxPeak)

    return maxPeak

test_cases = {
    'test_case_1': {
        'description': 'normal test',
        'input': [1, 2, 3, 3, 4, 0, 10, 6, 5, -1, -3, 2, 3],
        'output': 6,
        'active': True
    },
    'test_case_2': {
        'description': 'normal test',
        'input': [5, 4, 3, 2, 1, 2, 1],
        'output': 3,
        'active': True
    }
}
for test_name, data in test_cases.items():

    print('Running -> {} -> {}'.format(test_name, data['description']))

    if data['active'] == False:
        print('Skipped!')
        continue

    input = data['input']
    result = longestPeak(input)
    if result == data['output']:
        print('Test passed!')
    else:
        print('Test fail')
        print('Expected Output: ', end="")
        print(data['output'])
        print('Actual Output: ', end="")
        print(result)
    print()
