#Solution 1
def selectSort(arr):

  for i in range(0, len(arr)):
    min = float("inf")
    indexOfMin = None

    for j in range(i, len(arr)):

      if arr[j] < min:
        indexOfMin = j
        min = arr[j]

    arr[i], arr[indexOfMin] = arr[indexOfMin], arr[i]

  return arr

#Solution 2
def selectSortMax(arr):

    i = 0

    while i < len(arr):

        indexOfMax = arr.index(max(arr[i:]))

        arr[i], arr[indexOfMax] = arr[indexOfMax], arr[i]
        i += 1

    return arr

print(selectSort([19, 19, 21, 1, 1, 1, 1, 1]))
