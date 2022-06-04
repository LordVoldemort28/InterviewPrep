def quickSort(arr):
    
    if len(arr) < 2:
        return arr
    else:
        pivot = arr[0]
        
        less = [item for item in arr[1:] if item <= pivot]
        greater = [item for item in arr[1:] if item > pivot]
        
        return quickSort(less) + [pivot] + quickSort(greater)


print(quickSort([3, 6, 2, 5, 9]))
print(quickSort([19, 19, 21, 1, 1, 1, 1, 1]))


