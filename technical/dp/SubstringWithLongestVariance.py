from itertools import permutations
from collections import Counter

"""
Solution taken from 
https://leetcode.com/problems/substring-with-largest-variance/discuss/2412313/Python-or-Kadene-Algo-or-with-explanation

Using Kadane algorithm

Choose two chars and convert them to 1 and -1
and calculate largest sum possible
"""
class Solution(object):
    def largestVariance(self, s):
        
        #Get count of each character
        chars = Counter(s)
        
        globalMax = 0
        
        for (a, b) in permutations(chars, 2):
            globalMax = max(self.kandane(a, b, s, chars), globalMax)
        
        return globalMax
    
    def kandane(self, a, b, s, chars):
        
        maxVariance, currentVariance = 0, 0
        aCount, bCount = chars[a], chars[b]
        isA, isB = False, False
        
        for char in s:
            
            if char != a and char != b:
                continue
            
            if currentVariance < 0 and aCount != 0 and bCount != 0:
                currentVariance = 0
                isA = False
                isB = False
            
            if char == a:
                currentVariance += 1
                aCount -= 1
                isA = True
                
                
            if char == b:
                currentVariance -= 1
                bCount -= 1
                isB = True
                
            if isA and isB:
                maxVariance = max(maxVariance, currentVariance)

        return maxVariance

test_cases = {
    'test_case_3': {
        'description': 'cycle test',
        'input': 'abbbcde',
        'output': 2,
        'active': True
    },
    'test_case_1': {
        'description': 'cycle test',
        'input': 'aababbb',
        'output': 3,
        'active': True
    },
    'test_case_2': {
        'description': 'cycle test',
        'input': 'abcde',
        'output': 0,
        'active': True
    }
}

for test_name, data in test_cases.items():

    print('Running -> {} -> {}'.format(test_name, data['description']))

    if data['active'] == False:
        print('Skipped!')
        continue

    input = data['input']
    result = Solution().largestVariance(input)
    if result == data['output']:
        print('Test passed!')
    else:
        print('Test fail')
        print('Expected Output: ', end="")
        print(data['output'])
        print('Actual Output: ', end="")
        print(result)
    print()
