class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        
        res = []
        
        stack = [("(", 1, 0)]
        
        while stack:
            
            path, l, r = stack.pop()

            if l-r < 0 or l > n or r > n:
                continue
            
            if l == n and r == n:
                res.append(path)

            stack.append((path+"(", l+1, r))
            stack.append((path+")", l, r+1))

        return res
    

test_cases = {
    'test_case_1': {
        'description': 'cycle test',
        'input': 3,
        'output': ["((()))", "(()())", "(())()", "()(())", "()()()"],
        'active': True
    }
}

for test_name, data in test_cases.items():

    print('Running -> {} -> {}'.format(test_name, data['description']))

    if data['active'] == False:
        print('Skipped!')
        continue

    input = data['input']
    result = Solution().generateParenthesis(input)
    if sorted(result) == sorted(data['output']):
        print('Test passed!')
    else:
        print('Test fail')
        print('Expected Output: ', end="")
        print(data['output'])
        print('Actual Output: ', end="")
        print(result)
    print()
