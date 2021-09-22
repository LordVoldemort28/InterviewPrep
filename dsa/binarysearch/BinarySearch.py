"""
Easiest implementation of binary search in python

Works on divide and conquer approach and relies on the 
fact that array is sorted.

Time complexity: O(logN)
Space complexity: O(1)

Credit: Olivera Popović
Modified by: Rahul Prajapati
Source: https://stackabuse.com/binary-search-in-python/
Bonus: https://www.tutorialspoint.com/what-are-the-differences-between-recursion-and-iteration-in-java
"""
def binary_search_recursive(arr, element, low, high):

    if low > high:
        return False

    mid = (low + high) // 2

    if element == arr[mid]:
        return mid

    if element < arr[mid]:
        return binary_search_recursive(arr, element, low, mid-1)
    else:
        return binary_search_recursive(arr, element, mid+1, high)


def binary_search_iterative(arr, element, low, high):

    while low <= high:

        mid = (low + high) // 2

        if element == arr[mid]:
            return mid

        if element < arr[mid]:
            high = mid - 1
        else:
            low = mid + 1

    return -1


def contains(ordered_list, number):

    # Check if an integer is present in the list
    return binary_search_iterative(ordered_list, number, 0, len(ordered_list)-1)


print(contains([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 11))
