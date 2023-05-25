class Solution(object):

    def longestPalindrome(self, s):

        maxSize = 1
        n = len(s)
        result = s[0]
        
        for i in range(n):
            for j in range(i+1, n+1):
                substring = s[i:j]
                
                if substring == substring[::-1] and len(substring) > maxSize:
                    maxSize = len(substring)
                    result = substring
            
        return result


test_cases = {
    'test_case_1': {
        'description': 'cycle test',
        'input': "babad",
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
    result = Solution().longestPalindrome(input)
    if result == data['output']:
        print('Test passed!')
    else:
        print('Test fail')
        print('Expected Output: ', end="")
        print(data['output'])
        print('Actual Output: ', end="")
        print(result)
    print()
