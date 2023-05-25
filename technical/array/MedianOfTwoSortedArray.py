def findMedianSortedArrays(nums1, nums2):
    n1 = len(nums1)
    n2 = len(nums2)
    
    if n1 > n2:
        return findMedianSortedArrays(nums2, nums1)

    lo = 0
    hi = n1
    pos = ((n1 + n2) + 1) // 2

    while lo <= hi:

        mid1 = (lo + hi) // 2
        mid2 = pos - mid1

        l1 = float('-inf') if mid1 == 0 else nums1[mid1 - 1]
        l2 = float('-inf') if mid2 == 0 else nums2[mid2 - 1]
        r1 = float('inf') if mid1 == n1 else nums1[mid1]
        r2 = float('inf') if mid2 == n2 else nums2[mid2]

        if l1 <= r2 and l2 <= r1:
            if (n1 + n2) % 2 == 0:
                return (max(l1, l2) + min(r1, r2)) / 2
            else:
                return max(l1, l2)

        elif l1 > r2:
            hi = mid1 - 1
        else:
            lo = mid1 + 1

def findMedianSortedArraysBruteForce(num1, num2):
    num3 = num1 + num2
    num3.sort()
    mid = (len(num3)-1)//2

    if len(num3)%2 == 0:
        return (num3[mid] + num3[mid+1])/2
    else:
        return num3[mid]
    
# print(findMedianSortedArrays([1, 3, 5], [2, 4, 6]) == 3.5)
# print(findMedianSortedArraysBruteForce([1, 3, 5], [2, 4, 6]) == 3.5)
# print(findMedianSortedArrays([1, 3, 5], [2, 4, 6, 7]) == 4)
# print(findMedianSortedArraysBruteForce([1, 3, 5], [2, 4, 6, 7]) == 4)
print(findMedianSortedArraysBruteForce([1, 2], [3, 4]) == 2.5)
