def KadaneAlgorithm(array):
    
    maxSum = float("-inf")
    currSum = 0
    
    for el in array:
        
        currSum += el
        maxSum = max(currSum, maxSum)
        if currSum < 0: currSum = 0
        
    return maxSum

print(KadaneAlgorithm([-5,4,6,-3,4,-1]))