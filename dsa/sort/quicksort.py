"""
Easiest implentation of quicksort algorithm

It divides and conquer also decrease and conquer algorithm

It picks an element as pivot and partition the given array around the
picked pivot.

Different ways of picking pivots:
    1. Always picks first elements as pivot
    2. Always picks last elements as pivot
    3. Pick a random element as pivot
    4. Pick median as pivot(IDEAL!)
    
!!!Game of partition!!!!

After the target parition is given an array and as element X of
array as pivot. Put x as its correct position in sorted array and 
put all smaller elements (smaller than x) before x and put all greater
elements (greater than x) after x. 

Advantage: Space complexity
Modified by: Rahul Prajapati
Bonus: https://yongdanielliang.github.io/animation/web/QuickSortNew.html
Time Complexity: O(nlogn)
Space Complexity: O(1)
"""

def partition_at_last(arr, low, high):
    #pointer to track value to swap from
    i = low-1
    
    #Taking last element as pivot
    pivot = arr[high]
    
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            #swap values if current value is less than pivot
            arr[i], arr[j] = arr[j], arr[i]

    #swap last element with last i value plus 1
    arr[i+1], arr[high] = arr[high], arr[i+1]
    return i+1

def partition_at_first(arr, low, high):

    pivot = arr[low]
    start, end = low, high

    while start < end:
        while start < len(arr) and arr[start] <= pivot:
            start += 1
        while arr[end] > pivot:
            end -= 1
        if start < end:    
            arr[start], arr[end] = arr[end], arr[start]

    arr[low], arr[end] = arr[end], arr[low]

    return end

def quickSort(arr, low, high):

    if low < high:
        
        pi = partition_at_last(arr, low, high)

        quickSort(arr, low, (pi-1))
        quickSort(arr, (pi+1), high)

# arr = [87, 2, 56, 3, 34, 5, 28, 4]
# quickSort(arr, 0, len(arr)-1)
# print(arr)
# arr = [6,5,8,9,3,10,15,12,16]
# quickSort(arr, 0, len(arr)-1)
# print(arr)

arr = [87, 2, 56, 3, 34, 5, 28, 4]
quickSort(arr, 3, 6)
print(arr)
