class Solution:
    def totalStrengthBruteForce(self, strength):
        n = len(strength)
        points = 0
        
        for window in range(1, n+1):
            for i in range(n):
                if (i+window) > n: continue
                    
                subArray = strength[i: (i+window)]
                points += min(subArray) * sum(subArray)
                
        return points
    
    def totalStrength(self, strength):
        pass

test_cases = {
    'test_case_1': {
        'description': 'cycle test',
        'input': [1, 3, 1, 2],
        'output': 44,
        'active': True
    },
    'test_case_2': {
        'description': 'cycle test',
        'input': [5, 4, 6],
        'output': 213,
        'active': True
    },
    'test_case_3': {
        'description': 'cycle test',
        'input': [747, 812, 112, 1230, 1426, 1477, 1388, 976, 849, 1431, 1885, 1845, 1070, 1980, 280, 1075, 232, 1330, 1868, 1696, 1361, 1822, 524, 1899, 1904, 538, 731, 985, 279, 1608, 1558, 930, 1232, 1497, 875, 1850, 1173, 805,
                  1720, 33, 233, 330, 1429, 1688, 281, 362, 1963, 927, 1688, 256, 1594, 1823, 743, 553, 1633, 1898, 1101, 1278, 717, 522, 1926, 1451, 119, 1283, 1016, 194, 780, 1436, 1233, 710, 1608, 523, 874, 1779, 1822, 134, 1984],
        'output': 471441678,
        'active': True
    }
}

for test_name, data in test_cases.items():

    print('Running -> {} -> {}'.format(test_name, data['description']))

    if data['active'] == False:
        print('Skipped!')
        continue

    input = data['input']
    result = Solution().totalStrength(input)
    if result == data['output']:
        print('Test passed!')
    else:
        print('Test fail')
        print('Expected Output: ', end="")
        print(data['output'])
        print('Actual Output: ', end="")
        print(result)
    print()
