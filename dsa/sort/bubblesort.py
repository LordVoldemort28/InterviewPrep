def bubbleSort(array):

    #Swap element index
    i = 0

    while i < len(array):

        #Getting minimum element from swap idx till end
        minIdx = i
        min = array[minIdx]

        for idx in range(i, len(array)):

            if array[idx] < min:
                min = array[idx]
                minIdx = idx

        array[i], array[minIdx] = array[minIdx], array[i]
        i += 1

    return array


print(bubbleSort([19, 19, 21, 1, 1, 1, 1, 1]))
print(bubbleSort([87, 2, 56, 3, 34, 5, 28, 4]))
