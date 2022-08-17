from heapq import heapify, heappop
from heapq import heappush, heappop, heapify


class HeapNode:

    def __init__(self, arrayIdx, elementIdx, num):
        self.arrayIdx = arrayIdx
        self.elementIdx = elementIdx
        self.num = num

    def __lt__(self, node):
        return self.num < node.num


def mergeSortedArrays(arrays):

    n = len(arrays)
    
    heap = []
    
    #SortedList
    result = []

    #Insert first element of each list
    for idx in range(n):

        if len(arrays[idx]) > 0:
            heappush(heap, HeapNode(idx, 0, arrays[idx][0]))

    while heap:
        
        #Pop smallest
        currentNode = heappop(heap)
        
        #Unpack all elements
        arrayIdx, elementIdx, num = currentNode.arrayIdx, currentNode.elementIdx, currentNode.num
        
        #Add to final result
        result.append(num)

        #If its a last element of array then don't do anything
        if elementIdx == len(arrays[arrayIdx])-1:
            continue

        #else push next element of that array
        currentElementIdx = elementIdx+1
        heappush(heap, HeapNode(arrayIdx, currentElementIdx,
                 arrays[arrayIdx][currentElementIdx]))

    return result


def mergeSortedArraysBruteForce(arrays):

    totalLength = 0
    n = len(arrays)

    result = []

    for idx in range(n):
        heapify(arrays[idx])
        totalLength += len(arrays[idx])

    for _ in range(totalLength):

        minElement, minElementArrayIdx = float('inf'), 0

        for idx in range(n):

            if len(arrays[idx]) > 0 and arrays[idx][0] < minElement:
                minElementArrayIdx = idx
                minElement = arrays[idx][0]

        result.append(heappop(arrays[minElementArrayIdx]))

    return result


test_cases = {
    'test_case_1': {
        'description': 'cycle test',
        'input': [
            [1, 5, 9, 21],
            [-1, 0],
            [-124, 81, 121],
            [3, 6, 12, 20, 150]
        ],
        'output': [-124, -1, 0, 1, 3, 5, 6, 9, 12, 20, 21, 81, 121, 150],
        'active': True
    }
}

for test_name, data in test_cases.items():

    print('Running -> {} -> {}'.format(test_name, data['description']))

    if data['active'] == False:
        print('Skipped!')
        continue

    input = data['input']
    result = mergeSortedArrays(input)
    if result == data['output']:
        print('Test passed!')
    else:
        print('Test fail')
        print('Expected Output: ', end="")
        print(data['output'])
        print('Actual Output: ', end="")
        print(result)
    print()
