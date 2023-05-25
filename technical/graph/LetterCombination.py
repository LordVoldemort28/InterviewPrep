class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """

        all_paths = []

        size = len(digits)

        letters = {
            2: "abc",
            3: "def",
            4: "ghi",
            5: "jkl",
            6: "mno",
            7: "pqrs",
            8: "tuv",
            9: "wxyz"
        }

        def dfs(digitIndex, path):

            if digitIndex == size:
                all_paths.append(path)
                return

            current_digit = letters[int(digits[digitIndex])]

            for alphabet in current_digit:

                dfs(digitIndex+1, path+alphabet)

        dfs(0, "")

        return all_paths


tool = Solution()
print(tool.letterCombinations("78"))
