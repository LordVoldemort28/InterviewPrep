class NumberOfDigit:
    def findNumbers(self, nums):

        if len(nums) == 0:
            return 0

        count = 0

        for num in nums:

            if not len(str(nums)) % 2:
                count += 1

        return count


example1 = [12, 345, 2, 6, 7896]
example2 = [252]
sol = NumberOfDigit()
sol.findNumbers(example1)
