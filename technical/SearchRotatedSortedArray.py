class Solution(object):
    def searchBruteForce(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        # if len(nums) == 1:
        #     return 0 if nums[0] == target else -1

        def binarySearch(array, target, low, high):

            if low > high:
                return -1

            mid = (low+high)//2

            if array[mid] == target:
                return mid

            if array[mid] > target:
                return binarySearch(array, target, low, mid-1)
            else:
                return binarySearch(array, target, mid+1, high)
        
        pivotIndex = nums.index(min(nums))
        
        left = binarySearch(nums, target, 0, pivotIndex-1)
        
        if left != -1:
            return left
        
        return binarySearch(nums, target, pivotIndex, len(nums)-1)

    def search(self, nums, target):
        """
        Approach: Absolute truth that from mid there has to be one side which sorted
        """
        
        low, high = 0, len(nums)-1

        while low <= high:

            mid = (low+high)//2

            if nums[mid] == target:
                return mid

            #Check if left side is sorted or not
            if nums[low] <= nums[mid]:
                
                #If value exist on left side
                if nums[low] <= target <= nums[mid]:
                    high = mid - 1
                #Otherwise search on right side
                else:
                    low = mid + 1
            #Same as on right side if its sorted
            else:
                if nums[mid] <= target <= nums[high]:
                    low = mid + 1
                else:
                    high = mid - 1

        return -1

    
        

print(Solution().search([4, 5, 6, 7, 0, 1, 2], 0))
print(Solution().search([4, 5, 6, 7, 0, 1, 2], 100))
print(Solution().search([1], 1))
