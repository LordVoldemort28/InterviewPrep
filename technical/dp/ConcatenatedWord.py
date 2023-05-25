#https://leetcode.com/problems/word-break/
class Solution(object):
    def isWordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """

        dp = [False] * (len(s)+1)
        dp[0] = True

        for i in range(1, len(s)+1):

            for j in range(0, i):
                if dp[j] and s[j:i] in wordDict:
                    dp[i] = True
                    break

        return dp[-1]

    def findAllConcatenatedWordsInADict(self, words):
        
        result = []
        
        preWord = set()
        words.sort(key=len)

        for word in words:
            
            if self.isWordBreak(word, preWord):
                result.append(word)
            preWord.add(word)

        return result

test_cases = {
    'test_case_1': {
        'description': 'cycle test',
        'input': ["cat","cats","catsdogcats","dog","dogcatsdog","hippopotamuses","rat","ratcatdogcat"],
        'output': ['dogcatsdog', 'catsdogcats', 'ratcatdogcat'],
        'active': True
    },
    'test_case_2': {
        'description': 'cycle test',
        'input': ["cat", "dog", "catdog"],
        'output': ["catdog"],
        'active': True
    }
}

for test_name, data in test_cases.items():

    print('Running -> {} -> {}'.format(test_name, data['description']))

    if data['active'] == False:
        print('Skipped!')
        continue

    input = data['input']
    result = Solution().findAllConcatenatedWordsInADict(input)
    if result == data['output']:
        print('Test passed!')
    else:
        print('Test fail')
        print('Expected Output: ', end="")
        print(data['output'])
        print('Actual Output: ', end="")
        print(result)
    print()
