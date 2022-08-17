"""
Insertion sort
Time complexity -> O(n^2)
Space complexity -> O(1)
"""
def insertionSort(arr):
    for i in range(len(arr)):
        for j in range(0, (len(arr)-i-1)):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

print(insertionSort([19, 19, 21, 1, 1, 1, 1, 1]))
print(insertionSort([87, 2, 56, 3, 34, 5, 28, 4]))
