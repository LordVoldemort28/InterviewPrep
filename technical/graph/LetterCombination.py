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

        def dfs(index, path):

            if index == size:
                all_paths.append(path)
                return

            current_digit = letters[int(digits[index])]

            for alphabet in current_digit:

                dfs(index+1, path+alphabet)

        dfs(0, "")

        return all_paths


tool = Solution()
print(tool.letterCombinations("78"))
