class Solution(object):
    def maxArea(self, height):
        
        """
        Going with two pointer approach
        
        Put left and right pointer to each end of heights
        
        while coming from both ends maintain global max height
        
            calculate max area
            move left or right pointer based on greater height
        """
        
        left = 0 
        right = len(height)-1
        maxArea = float("-inf")
        
        while left < right:
            
            currentLength = right - left
            currentHeight = min(height[right], height[left])
            
            maxArea = max((currentLength*currentHeight), maxArea)
            
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
                
        return maxArea 


test_cases = {
    'test_case_1': {
        'description': 'cycle test',
        'input': [1, 8, 6, 2, 5, 4, 8, 3, 7],
        'output': 49,
        'active': True
    },
    'test_case_2': {
        'description': 'cycle test',
        'input': [1, 1],
        'output': 1,
        'active': True
    }
}

for test_name, data in test_cases.items():

    print('Running -> {} -> {}'.format(test_name, data['description']))

    if data['active'] == False:
        print('Skipped!')
        continue

    input = data['input']
    result = Solution().maxArea(input)
    if result == data['output']:
        print('Test passed!')
    else:
        print('Test fail')
        print('Expected Output: ', end="")
        print(data['output'])
        print('Actual Output: ', end="")
        print(result)
    print()
