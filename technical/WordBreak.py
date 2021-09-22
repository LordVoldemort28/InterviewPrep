class Solution(object):
    def wordBreak(self, s, wordDict):
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
        print(dp)
        return dp[len(s)]


input = ["leet", "code"]
tool = Solution()
print(tool.wordBreak("leetcode", input))