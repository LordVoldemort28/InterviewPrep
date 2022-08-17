def midTraversal(arr, low, high, result=[]):
    
    if low <= high:
        
        mid = (low+high)//2
        
        result.append(arr[mid])
        midTraversal(arr, low, mid-1)
        midTraversal(arr, mid+1, high)
    
    return result

input = [1, 2, 5, 7, 10, 13, 14, 15, 22]
low = 0
high = len(input)-1

#[10, 2, 1, 5, 7, 14, 13, 15, 22]
print(midTraversal(input, low, high))
