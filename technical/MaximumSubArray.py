import math

def minSubArrayLen(s, nums):
    out = math.inf
    add = 0
    start = 0

    #Sliding window approach
    for i, num in enumerate(nums):
        #Expand window
        add += num
        #Add until local sum gets greater than or equal to target value
        while add >= s:
            #Subtract start index element of window
            add -= nums[start]
            
            #Update minimum number of element in window
            out = min(out, i+1-start)
            
            #Move start index of window to left
            start += 1

    return out if out != math.inf else -1


print(minSubArrayLen(6, [1, 2, 3, 4]))
print(minSubArrayLen(51, [1, 4, 45, 6, 0, 19]))
print(minSubArrayLen(4, [1, 2, 3]))
