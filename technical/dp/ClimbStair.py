#Fibonacci with tail recursion

class Solution(object):

    def climbStairs(self, n):

        a, b = 0, 1

        for _ in range(1, (n+1)):

            a, b = b, (a+b)

        return b
