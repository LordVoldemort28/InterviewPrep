#Two sum
def threeSum(nums):
    """
    :type nums: List[int]
    :rtype: List[List[int]]
    """
    result = []
    nums = sorted(nums)

    for i in range(0, len(nums)):

        temp = twoSum(i, nums)

        if temp != -1:
            temp = sorted(temp)
            if temp not in result:
                result.append(temp)

    return result


def twoSum(targetIdx, arr):

    low, high, target = 0, len(arr)-1, -arr[targetIdx]
    result = []
    while low < high:

        sum = arr[low] + arr[high]

        if target == sum and low != targetIdx and high != targetIdx:
            result.append([-target, arr[low], arr[high]])
        elif sum > target:
            high -= 1
        else:
            low += 1

    if len(result) != 0:
      return result

    return -1


print(twoSum(target, sorted(arr)))
#[[-4,0,4],[-4,1,3],[-3,-1,4],[-3,0,3],[-3,1,2],[-2,-1,3],[-2,0,2],[-1,-1,2],[-1,0,1]]

arr = [-1, 0, 1, 2, -1, -4, -2, -3, 3, 0, 4]
target = -4
# print(sorted(arr))
# print(threeSum(arr))
