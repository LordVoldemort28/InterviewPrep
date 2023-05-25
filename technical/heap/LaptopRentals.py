from heapq import heappush, heapreplace

def laptopRentals(times):
    times.sort()
    heap = []
    
    for (start, end) in times:
        
        if heap and start >= heap[0]:
            heapreplace(heap, end)
        #Add laptop
        else:
            heappush(heap, end)
        
    return len(heap)


test_cases = {
    'test_case_1': {
        'description': 'cycle test',
        'input': [
            [0, 2],
            [1, 4],
            [4, 6],
            [0, 4],
            [7, 8],
            [9, 11],
            [3, 10]
        ],
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
    result = laptopRentals(input)
    if result == data['output']:
        print('Test passed!')
    else:
        print('Test fail')
        print('Expected Output: ', end="")
        print(data['output'])
        print('Actual Output: ', end="")
        print(result)
    print()
