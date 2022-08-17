class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """

        dp = [float("inf")] * (amount+1)
        dp[0] = 0

        for idx in range(1, amount+1):

            for coin in coins:

                if idx-coin >= 0:

                    dp[idx] = min(dp[idx], dp[idx-coin]+1)

        return -1 if dp[-1] == float("inf") else dp[-1]


coins = [1, 2, 5]
amount = 11

tool = Solution()
result = tool.coinChange(coins, amount)
print(result)