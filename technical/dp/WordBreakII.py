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

        return dp
    
    def wordBreak(self, s, words):
        
        result = []
        dp = self.isWordBreak(s, words)
        
        if not dp[-1]:
            return result
        
        def dfs(s, path):
            
            if not s:
                result.append(" ".join(path))
            else:
                for i in range(1, len(s)+1):
                    if s[:i] in words:
                        dfs(s[i:], path + [s[:i]])
        
        dfs(s, [])
        
        return result


test_cases = {
    'test_case_1': {
        'description': 'cycle test',
        'input': {
            's': 'leetcodet',
            'words': ["leet", "code", "t"]
        },
        'output': ['leet code t'],
        'active': True
    },
    'test_case_2': {
        'description': 'cycle test',
        'input': {
            's': 'catsdogcats',
            'words': ["cat", "cats", "catsdogcats", "dog", "dogcatsdog", "hippopotamuses", "rat", "ratcatdogcat"]
        },
        'output': ['cats dog cats', 'catsdogcats'],
        'active': True
    },
    'test_case_3': {
        'description': 'normal test',
        'input': {
            's': 'rockstar',
            'words': ["rock", "rockstar", "star", "rocks", "tar"]
        },
        'output': ['rock star', 'rocks tar', 'rockstar'],
        'active': True
    }
}

for test_name, data in test_cases.items():

    print('Running -> {} -> {}'.format(test_name, data['description']))

    if data['active'] == False:
        print('Skipped!')
        continue

    input = data['input']
    result = Solution().wordBreak(input['s'], input['words'])
    if result == data['output']:
        print('Test passed!')
    else:
        print('Test fail')
        print('Expected Output: ', end="")
        print(data['output'])
        print('Actual Output: ', end="")
        print(result)
    print()
