def mergeOverlappingIntervals(intervals):
    # Write your code here.
    if len(intervals) < 2:
        return intervals

    #Sort interval using start time
    intervals.sort()

    current = intervals[0]
    results = [current]

    for idx in range(1, len(intervals)):

        _, end = current
        nextStart, nextEnd = intervals[idx]
        
        #Checking if next interval has merging range from current end
        #current = [2, 4] and next = [3, 5] then current = [2, 5]
        if end >= nextStart:
            current[1] = max(end, nextEnd)
        else:
            current = intervals[idx]
            results.append(current)

    return results


test_cases = {
    'test_case_1': {
        'description': 'cycle test',
        'input': [
            [1, 2],
            [3, 5],
            [4, 7],
            [6, 8],
            [9, 10]
        ],
        'output': [[1, 2], [3, 8], [9, 10]],
        'active': True
    }
}

for test_name, data in test_cases.items():

    print('Running -> {} -> {}'.format(test_name, data['description']))

    if data['active'] == False:
        print('Skipped!')
        continue

    input = data['input']
    result = mergeOverlappingIntervals(input)
    if result == data['output']:
        print('Test passed!')
    else:
        print('Test fail')
        print('Expected Output: ', end="")
        print(data['output'])
        print('Actual Output: ', end="")
        print(result)
    print()
