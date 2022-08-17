# Implementing merge sort from scratch
# Author: Rahul Prajapati

# MergeSort(arr[], l,  r)
# If r > l
#      1. Find the middle point to divide the array into two halves:
#              middle m = l+ (r-l)/2
#      2. Call mergeSort for first half:
#              Call mergeSort(arr, l, m)
#      3. Call mergeSort for second half:
#              Call mergeSort(arr, m+1, r)
#      4. Merge the two halves sorted in step 2 and 3:
#              Call merge(arr, l, m, r)

# Recursive function: T(n) = 2T(n/2) + O(n)
# Auxiliary Space: O(n)
# Time Complexity: O(nlogn)
# Algorithmic Paradigm: Divide and Conquer
# Sorting In Place: No in a typical implementation
# Stable: Yes

def merge(arr, left, right):

    i = j = k = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            j += 1
        k += 1

    while i < len(left):
        arr[k] = left[i]
        k += 1
        i += 1

    while j < len(right):
        arr[k] = right[j]
        k += 1
        j += 1

    return arr


def mergeSort(arr):

    if len(arr) > 1:

        middle = len(arr)//2

        left = arr[:middle]

        right = arr[middle:]

        mergeSort(left)

        mergeSort(right)

        return merge(arr, left, right)


def main():
    arr = [87, 2, 56, 3, 34, 5, 28, 4]
    sorted_arr = mergeSort(arr)
    print(sorted_arr)
    return


if __name__ == '__main__':
    main()
