class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """

        for i in range(1, len(triangle)):
            for j in range(0, len(triangle[i])):

                cost_diagonal = float("inf") if j-1 < 0 else triangle[i-1][j-1]
                cost_up = float("inf") if j < 0 or j > len(
                    triangle[i-1])-1 else triangle[i-1][j]

                triangle[i][j] = triangle[i][j] + min(cost_up, cost_diagonal)

        return min(triangle[-1])


triangle = [[2], [3, 4], [6, 5, 7], [4, 1, 8, 3]]
tool = Solution()
print(tool.minimumTotal(triangle))