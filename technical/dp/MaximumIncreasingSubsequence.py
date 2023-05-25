def maxSumIncreasingSubsequence(arr):

    n = len(arr)
    
    #Storing current max
    maxSum = arr.copy()
    
    #Storing where max came from for backtracking
    actual = [i for i in range(n)]

    #Loop like
    #j ->     i 
    #1, 2, 5, 3, 9
    for i in range(1, n):
        for j in range(0, i):
            
            #If ith element is bigger than jth element its look candidate for increasing subsequence
            #Then we also have to check jth best max sum to get overall best
            if arr[j] < arr[i] and maxSum[j] + arr[i] > maxSum[i]:
                maxSum[i] = maxSum[j] + arr[i]
                actual[i] = j

    #Backtracking
    start = maxSum.index(max(maxSum))
    result = []
    while True:

        result += [arr[start]]

        if start == actual[start]:
            break

        start = actual[start]

    return [max(maxSum), result[::-1]]
