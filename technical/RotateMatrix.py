class Solution:
    def rotate(self, matrix):

        n = len(matrix)

        #Transpose (diagonally rotate)
        for i in range(n):
            for j in range(i, n):
                matrix[j][i], matrix[i][j] = matrix[i][j], matrix[j][i]

        #Flip (rotate vertically)
        for i in range(n):
            for j in range(n // 2):
                matrix[i][j], matrix[i][-j-1] = matrix[i][-j-1], matrix[i][j]
            
test_cases = {
    'test_case_1': {
        'description': 'cycle test',
        'input': [
            [5, 1, 9, 11], 
            [2, 4, 8, 10],
            [13, 3, 6, 7], 
            [15, 14, 12, 16]
        ],
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
    result = Solution().rotate(input)
    if result == data['output']:
        print('Test passed!')
    else:
        print('Test fail')
        print('Expected Output: ', end="")
        print(data['output'])
        print('Actual Output: ', end="")
        print(result)
    print()
