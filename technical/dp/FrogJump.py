from functools import cache

#Frog jump

class Solution(object):
    def canCross(self, stones):
        """
        :type stones: List[int]
        :rtype: bool
        """
        #Approach is dfs+dp
        
        if stones[1] - stones[0] != 1:
            return False
        
        startStone = stones[1]
        lastStone = stones[-1]
        
        #For faster lookups
        stones = set(stones)
        
        @cache
        def dfs(stone, k):
            
            #Base case if stone is last stone in river
            if stone == lastStone:
                return True
            
            #Jumping in from k-1 to k+1
            for j in range(k-1, k+2):
                
                jumpPosition = stone + j
                
                if j > 0 and jumpPosition in stones and dfs(jumpPosition, j):
                    return True
            
            return False
        
        return dfs(startStone, 1)
    

test_cases = {
    'test_case_1': {
        'description': 'cycle test',
        'input': [0, 1, 3, 5, 6, 8, 12, 17],
        'output': True,
        'active': True
    },
    'test_case_2': {
        'description': 'cycle test',
        'input': [0, 1, 2, 3, 4, 8, 9, 11],
        'output': False,
        'active': True
    }
}

for test_name, data in test_cases.items():

    print('Running -> {} -> {}'.format(test_name, data['description']))

    if data['active'] == False:
        print('Skipped!')
        continue

    input = data['input']
    result = Solution().canCross(input)
    if result == data['output']:
        print('Test passed!')
    else:
        print('Test fail')
        print('Expected Output: ', end="")
        print(data['output'])
        print('Actual Output: ', end="")
        print(result)
    print()
