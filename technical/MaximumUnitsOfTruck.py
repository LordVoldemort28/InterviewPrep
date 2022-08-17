class Solution:
    def maximumUnits(self, boxTypes, truckSize):
        boxTypes.sort(key=lambda x: x[1], reverse=1)
        s = 0
        for i, j in boxTypes:
            i = min(i, truckSize)
            s += i*j
            truckSize -= i
            if truckSize == 0:
                break
        return s


test_cases = {
    'test_case_1': {
        'description': 'cycle test',
        'input': ([[5, 10], [2, 5], [4, 7], [3, 9]], 10),
        'output': 91,
        'active': True
    }
}

for test_name, data in test_cases.items():

    print('Running -> {} -> {}'.format(test_name, data['description']))

    if data['active'] == False:
        print('Skipped!')
        continue

    input = data['input']
    result = Solution().maximumUnits(input[0], input[1])
    if result == data['output']:
        print('Test passed!')
    else:
        print('Test fail')
        print('Expected Output: ', end="")
        print(data['output'])
        print('Actual Output: ', end="")
        print(result)
    print()
