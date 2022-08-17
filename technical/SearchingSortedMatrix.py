"""
Brute force
Approach: Loop each row in matrix and check if element range
falls within target range do binary search
Time complexity: O(mlogn) 
Space complexity: O(1)

Where m is number of rows and n number of elements in each row
"""
def searchInSortedMatrix2(matrix, target):
    
    for idx, arr in enumerate(matrix):
        
        low, high = 0, len(arr)-1
        
        if target >= arr[low] and target <= arr[high]:
            
            result = binary_search_recursive(arr, target, low, high)
            
            if result != -1:
                return [idx, result]
            
    return [-1, -1]


def binary_search_recursive(arr, element, low, high):

    if low > high:
        return -1

    mid = (low + high) // 2

    if element == arr[mid]:
        return mid

    if element < arr[mid]:
        return binary_search_recursive(arr, element, low, mid-1)
    else:
        return binary_search_recursive(arr, element, mid+1, high)

def searchInSortedMatrix(matrix, target):
    
    rowLen, colLen = len(matrix), len(matrix[0]) 
    row, col = 0, colLen-1
    
    while row in range(rowLen) and col in range(colLen):
        element = matrix[row][col]
        if target < matrix[row][col]:
            col -= 1
        elif target > matrix[row][col]:
            row += 1
        else:
            return [row, col]
    return [-1, -1]

test_cases = {
    'test_case_1': {
        'description': 'cycle test',
        'input': {
            'matrix': [
                [1, 4, 7, 12, 15, 1000],
                [2, 5, 19, 31, 32, 1001],
                [3, 8, 24, 33, 35, 1002],
                [40, 41, 42, 44, 45, 1003],
                [99, 100, 103, 106, 128, 1004]
            ],
            'target': 44
        },
        'output': [3, 3],
        'active': True
    },
    'test_case_2': {
        'description': 'not found test',
        'input': {
            'matrix': [
                [1, 4, 7, 12, 15, 1000],
                [2, 5, 19, 31, 32, 1001],
                [3, 8, 24, 33, 35, 1002],
                [40, 41, 42, 44, 45, 1003],
                [99, 100, 103, 106, 128, 1004]
            ],
            'target': -1
        },
        'output': [-1, -1],
        'active': True
    }
}

for test_name, data in test_cases.items():

    print('Running -> {} -> {}'.format(test_name, data['description']))

    if data['active'] == False:
        print('Skipped!')
        continue

    input = data['input']
    result = searchInSortedMatrix(input['matrix'], input['target'])
    if result == data['output']:
        print('Test passed!')
    else:
        print('Test fail')
        print('Expected Output: ', end="")
        print(data['output'])
        print('Actual Output: ', end="")
        print(result)
    print()
