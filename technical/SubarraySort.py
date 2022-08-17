"""
Time complexity - O(nlogn)
Space complexity - O(n)
"""
def subarraySortBruteForce(array):
    temp = sorted(array)
    minIdx = len(array)-1
    maxIdx = 0

    for idx in range(len(array)):
        if temp[idx] != array[idx]:
            minIdx = min(idx, minIdx)
            maxIdx = max(idx, maxIdx)
            
    if minIdx == len(array)-1 and maxIdx == 0:
        return [-1, -1]

    return [minIdx, maxIdx]

"""
bubble sort can be applied here with visited array to 
keep tracking of minimum
Time complexity -> O(n^2)
Space complexity -> O(1)
"""

"""
Solution: https://www.geeksforgeeks.org/minimum-length-unsorted-subarray-sorting-which-makes-the-complete-array-sorted/

Find the candidate unsorted subarray 
 - Scan from left to right and find the first element which is greater than the next element. Let s be the index of such an element. In the above example 1, s is 3 (index of 30). 
 - Scan from right to left and find the first element (first in right to left order) which is smaller than the next element (next in right to left order). Let e be the index of such an element. In the above example 1, e is 7 (index of 31).

Check whether sorting the candidate unsorted subarray makes the complete array sorted or not. If not, then include more elements in the subarray. 
 - Find the minimum and maximum values in arr[s..e]. Let minimum and maximum values be min and max. min and max for [30, 25, 40, 32, 31] are 25 and 40 respectively. 
 - Find the first element (if there is any) in arr[0..s-1] which is greater than min, change s to index of this element. There is no such element in above example 1. 
 - Find the last element (if there is any) in arr[e+1..n-1] which is smaller than max, change e to index of this element. In the above example 1, e is changed to 8 (index of 35)

Print s and e.

Time complexity -> O(n)
Space complexity -> O(1)
"""
def subarraySort(array):
    
    n = len(array)
    
    #Scan from left to right and find the first element which is greater than the next element.
    sorted = True
    for s in range(0, n-1):
        if array[s+1] < array[s]:
            sorted = False
            break

    #If minIdx is not means array is already sorted completely
    if sorted == True:
        return [-1, -1]
    
    #Scan from right to left and find the first element (first in right to left order) which is smaller than the next element (next in right to left order)
    for e in range(n-1, 0, -1):
        if array[e] < array[e-1]:
            break
        
    #Find the minimum and maximum values in arr[s..e].
    maxElement = max(array[(s+1):(e+1)])
    minElement = min(array[(s+1):(e+1)])
    
    for idx in range(0, s):
        if minElement < array[idx]:
            s = idx
            break
        

    i = n-1
    while i >= e+1:
        if array[i] < maxElement:
            e = i
            break
        i -= 1
    
    return [s, e]

test_cases = {
    'test_case_0': {
        'description': 'normal test',
        'input': [10, 12, 20, 30, 25, 40, 32, 31, 35, 50, 60],
        'output': [3, 8],
        'active': True
    },
    'test_case_1': {
        'description': 'normal test',
        'input': [1, 2, 4, 7, 10, 11, 7, 12, 7, 7, 16, 18, 19],
        'output': [4, 9],
        'active': True
    },
    'test_case_4': {
        'description': 'normal test',
        'input': [4, 8, 7, 12, 11, 9, -1, 3, 9, 16, -15, 11, 57],
        'output': [0, 11],
        'active': True
    },
    'test_case_2': {
        'description': 'already sorted test',
        'input': [1, 2],
        'output': [-1, -1],
        'active': True
    },
    'test_case_3': {
        'description': 'small array test',
        'input': [2, 1],
        'output': [0, 1],
        'active': True
    }
}

for test_name, data in test_cases.items():

    print('Running -> {} -> {}'.format(test_name, data['description']))

    if data['active'] == False:
        print('Skipped!')
        continue

    input = data['input']
    result = subarraySort(input)
    if result == data['output']:
        print('Test passed!')
    else:
        print('Test fail')
        print('Expected Output: ', end="")
        print(data['output'])
        print('Actual Output: ', end="")
        print(result)
    print()
