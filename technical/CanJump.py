class Solution:
    def canJump(self, nums) -> bool:

        current_idx = 0
        current_ele = nums[current_idx]

        while current_idx < len(nums) and current_ele != 0:

            current_ele = nums[current_idx]
            current_idx += current_ele

        if current_idx >= len(nums)-1:
            return True

        return False


tool = Solution()
print(tool.canJump([2, 3, 1, 1, 4]) == True)
print(tool.canJump([3, 2, 1, 0, 4]) == False)
print(tool.canJump([2, 0]) == True)
print(tool.canJump([0]) == True)
print(tool.canJump([2, 0, 0]) == True)
print(tool.canJump([2, 5, 0, 0]) == True)
