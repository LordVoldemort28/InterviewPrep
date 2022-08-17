def isValidSubsequence(array, sequence):
    # Write your code here.

	if not len(array):
		return False

	if not len(sequence):
		return True

	i, j = 0, 0

	while i < len(array) and j < len(sequence):

		if array[i] == sequence[j]:
			j += 1
		i += 1

	if j == len(sequence):
		return True

	return False


test_cases = {
    'test_case_1': {
        'description': 'cycle test',
        'input': {
            'array': [5, 1, 22, 25, 6, -1, 8, 10],
            'subsequence': [1, 6, -1, 10]
        },
        'output': True,
        'active': True
    }
}

for test_name, data in test_cases.items():

    print('Running -> {} -> {}'.format(test_name, data['description']))

    if data['active'] == False:
        print('Skipped!')
        continue

    input = data['input']
    result = isValidSubsequence(input['array'], input['subsequence'])
    if result == data['output']:
        print('Test passed!')
    else:
        print('Test fail')
        print('Expected Output: ', end="")
        print(data['output'])
        print('Actual Output: ', end="")
        print(result)
    print()
