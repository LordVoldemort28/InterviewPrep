from functools import cache

"""
Given 'budget' and prices for each category of ads (mxn int array), pick one price from each category and maximize the budget utilization

budget = 30
adPrices=
[3,1,5,7,10]
[7,9,2,20,10]
[3,1,9,45,51]
"""

class Solution(object):
    
    def minimizeTheDifference(self, mat, target):
        """
        :type mat: List[List[int]]
        :type target: int
        :rtype: int
        """
        m = len(mat)

        #Remove duplicates
        for i in range(m):
            mat[i] = set(mat[i])

        self.minDiff = float("inf")

        @cache
        def dfs(rowIdx, currentSum):

            if target + self.minDiff < currentSum:
                return float("inf")

            if rowIdx == m:
                return abs(target-currentSum)

            minDiff = float("inf")
            row = mat[rowIdx]

            for num in row:
                minDiff = min(minDiff, dfs((rowIdx+1), (currentSum+num)))

            self.minDiff = min(self.minDiff, minDiff)

            return minDiff

        dfs(0, 0)

        return self.minDiff
    
    def minimizeTheDifferenceWithoutCache(self, mat, target):
        """
        :type mat: List[List[int]]
        :type target: int
        :rtype: int
        """
        m = len(mat)
        
        #Remove duplicates
        for i in range(m):
            mat[i] = set(mat[i])
                
        self.minDiff = float("inf")
        dp = {}
        
        def dfs(rowIdx, currentSum):
            
            if (rowIdx, currentSum) in dp.keys():
                return dp[(rowIdx, currentSum)]
            
            if target + self.minDiff < currentSum:
                return float("inf")
            
            if rowIdx == m:
                return abs(target-currentSum)
            
            minDiff = float("inf")
            row = mat[rowIdx]
            
            for num in row:
                minDiff = min(minDiff, dfs((rowIdx+1), (currentSum+num)))
                
            self.minDiff = min(self.minDiff, minDiff)
            
            dp[(rowIdx, currentSum)] = minDiff
            return minDiff
        
        dfs(0, 0)
        
        return self.minDiff
    
    def minimizeTheDifferenceBruteForce(self, mat, target):
        """
        :type mat: List[List[int]]
        :type target: int
        :rtype: int
        """
        def dfs(mat, rowIdx, currentDiff, minDiff=float("inf")):

            if rowIdx == len(mat):
                return currentDiff

            for i in range(len(mat[0])):
                minDiff = min(minDiff, dfs(mat, (rowIdx+1),
                                abs(currentDiff-mat[rowIdx][i])))

            return minDiff

        return dfs(mat, 0, target)

test_cases = {
    'test_case_1': {
        'description': 'cycle test',
        'input': {
            'mat': [[1, 2, 3], [4, 5, 6], [7, 8, 9]],
            'target': 13
        },
        'output': 0,
        'active': True
    },
    'test_case_2': {
        'description': 'cycle test',
        'input': {
            'mat': [[1], [2], [3]],
            'target': 100
        },
        'output': 94,
        'active': True
    },
    'test_case_3': {
        'description': 'cycle test',
        'input': {
            'mat': [[1, 2, 9, 8, 7]],
            'target': 6
        },
        'output': 1,
        'active': True
    },
    'test_case_4': {
        'description': 'cycle test',
        'input': {
            'mat': [
                [3, 1, 5, 7, 10],
                [7, 9, 2, 20, 10],
                [3, 1, 9, 45, 51]
            ],
            'target': 30
        },
        'output': 0,
        'active': True
    },
}

for test_name, data in test_cases.items():

    print('Running -> {} -> {}'.format(test_name, data['description']))

    if data['active'] == False:
        print('Skipped!')
        continue

    input = data['input']
    result = Solution().minimizeTheDifferenceBruteForce(
        input['mat'], input['target'])
    if result == data['output']:
        print('Test passed!')
    else:
        print('Test fail')
        print('Expected Output: ', end="")
        print(data['output'])
        print('Actual Output: ', end="")
        print(result)
    print()
