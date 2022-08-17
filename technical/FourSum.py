#Brute force -> O(n^4)
from re import L


def fourNumberSumBruteForce(array, targetSum):
    result = []

    for i in range(len(array)):
        for j in range(len(array)):
            for k in range(len(array)):
                for l in range(len(array)):
                    items = sorted([array[i], array[j], array[k], array[l]])
                    if i != j and i != k and i != l \
                            and j != k and j != l \
                            and k != l \
                            and sum(items) == targetSum:
                        if items not in result:
                            result.append(items)
    return result


def threeSum(arr, target):

    arr.sort()
    results = []

    for idx in range(0, len(arr)-2):

        left = idx+1
        right = len(arr)-1

        while left < right:

            currentElements = [arr[idx], arr[left], arr[right]]
            currentSum = sum(currentElements)

            if currentSum == target:
                results.append(currentElements)
                left += 1
                right -= 1
            elif currentSum < target:
                left += 1
            else:
                right -= 1

    return results

def fourSum(arr, target):
    
    results = []
    
    for idx, item in enumerate(arr):
        
        #Slicing array such that it exclude current item
        excludeItemArray = arr[:idx] + arr[idx+1:]
        threeSumTarget = (target-item)
        threeSumResults = threeSum(excludeItemArray, threeSumTarget)
        
        for result in threeSumResults:
            
            fourSumResult = sorted(result + [item])
            
            if fourSumResult not in results:
                results.append(fourSumResult)
    
    return results

test_cases = {
    'test_case_1': {
        'description': 'normal test',
        'input': {
            'array': [7, 6, 4, -1, 1, 2],
            'target': 16
        },
        'output': [[-1, 4, 6, 7], [1, 2, 6, 7]],
        'active': True
    }
}

for test_name, data in test_cases.items():

    print('Running -> {} -> {}'.format(test_name, data['description']))

    if data['active'] == False:
        print('Skipped!')
        continue

    input = data['input']
    result = fourSum(input['array'], input['target'])
    if result == data['output']:
        print('Test passed!')
    else:
        print('Test fail')
        print('Expected Output: ', end="")
        print(data['output'])
        print('Actual Output: ', end="")
        print(result)
    print()
