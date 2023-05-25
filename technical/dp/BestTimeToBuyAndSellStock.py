class Solution(object):
    def maxProfitBruteForce(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        maxProfit = 0
        n = len(prices)

        for i in range(0, n):
            for j in range(i+1, n):

                if prices[i] < prices[j]:
                    maxProfit = max(maxProfit, (prices[j]-prices[i]))

        return maxProfit

    def maxProfit(self, prices):

        maxProfit = 0
        n = len(prices)

        left, right = 0, 1

        while right < n:

            if prices[right] > prices[left]:
                maxProfit = max(maxProfit, (prices[right]-prices[left]))
            else:
                left = right
            right += 1

        return maxProfit


test_cases = {
    'test_case_1': {
        'description': 'cycle test',
        'input': [7, 1, 5, 3, 6, 4],
        'output': 5,
        'active': True
    },
    'test_case_2': {
        'description': 'cycle test',
        'input': [7, 6, 4, 3, 1],
        'output': 0,
        'active': True
    }
}

for test_name, data in test_cases.items():

    print('Running -> {} -> {}'.format(test_name, data['description']))

    if data['active'] == False:
        print('Skipped!')
        continue

    input = data['input']
    result = Solution().maxProfit(input)
    if result == data['output']:
        print('Test passed!')
    else:
        print('Test fail')
        print('Expected Output: ', end="")
        print(data['output'])
        print('Actual Output: ', end="")
        print(result)
    print()
