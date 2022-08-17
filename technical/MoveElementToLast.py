def moveElementToEnd(array, toMove):
    # Write your code here.

	if len(array) < 2:
		return array

	current, last = 0, len(array)-1

	while current < last:

        #Shift right pointer from end to non toMove number
		while current < last and array[last] == toMove:
			last -= 1

        #If current is toMove number swap position
		if array[current] == toMove:

			array[current], array[last] = array[last], array[current]

		current += 1

	return array


test_cases = {
    'test_case_1': {
        'description': 'cycle test',
        'input': {
            'array': [2, 1, 2, 2, 2, 3, 4, 2],
            'toMove': 2
        },
        'output': [4, 1, 3, 2, 2, 2, 2, 2],
        'active': True
    }
}

for test_name, data in test_cases.items():

    print('Running -> {} -> {}'.format(test_name, data['description']))

    if data['active'] == False:
        print('Skipped!')
        continue

    input = data['input']
    result = moveElementToEnd(input['array'], input['toMove'])
    if result == data['output']:
        print('Test passed!')
    else:
        print('Test fail')
        print('Expected Output: ', end="")
        print(data['output'])
        print('Actual Output: ', end="")
        print(result)
    print()
