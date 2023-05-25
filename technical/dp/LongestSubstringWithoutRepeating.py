class Solution(object):
#Longest subsequence without repeating
    def lengthOfLongestSubstringBruteForce(self, s):
        unique = set()
        maxLength = float("-inf")

        for char in s:
            if char in unique:
                maxLength = max(maxLength, len(unique))
                unique = set()
            else:
                unique.add(char)
        maxLength = max(maxLength, len(unique))
        return maxLength

    def lengthOfLongestSubstring(self, s):

        left = maxLength = 0
        uniqueChars = {}

        for idx, char in enumerate(s):
            if char in uniqueChars and left <= uniqueChars[char]:
                left = uniqueChars[char] + 1
            else:
                maxLength = max(maxLength, idx - left + 1)

            uniqueChars[char] = idx

        return maxLength

test_cases = {
    'test_case_3': {
        'description': 'cycle test',
        'input': "pwwkew",
        'output': 3,
        'active': True
    },
    'test_case_1': {
        'description': 'cycle test',
        'input': "abcabcbb",
        'output': 3,
        'active': True
    },
    'test_case_2': {
        'description': 'cycle test',
        'input': "bbbbbb",
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
    result = Solution().lengthOfLongestSubstring(input)
    if result == data['output']:
        print('Test passed!')
    else:
        print('Test fail')
        print('Expected Output: ', end="")
        print(data['output'])
        print('Actual Output: ', end="")
        print(result)
    print()
