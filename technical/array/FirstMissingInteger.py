class Solution(object):
    def firstMissingPositive(self, nums):
        """
        T->O(max(n))
        S->O(1)
        """

        #Setting max range of the loop
        maxN = max(nums)
        
        #For faster lookup
        nums = set(nums)

        i = 1
        #Choosing while because in range is creating error for big range
        while i < maxN:
            
            #Returning first missing positive integer from given array
            if i not in nums:
                return i

            i += 1

        #If all positive exist then result should be next element of max
        #Otherwise if there's only negative elements then first positive has to be 1
        return maxN+1 if maxN > 0 else 1
    
