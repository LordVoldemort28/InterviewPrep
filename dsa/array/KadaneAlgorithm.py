def KadaneAlgorithmEasy(array):
    
    maxSum = float("-inf")
    currSum = 0
    
    for el in array:
        
        currSum += el
        maxSum = max(currSum, maxSum)
        if currSum < 0: currSum = 0
        
    return maxSum


def KadaneAlgorithm(array):

    maxSum = 0
    currSum = 0

    for el in array:

        maxSum = max((maxSum+el), el)
        currSum = max(currSum, maxSum)

    return maxSum


print(KadaneAlgorithmEasy([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
print(KadaneAlgorithmEasy([-1, -1, 1, -1, 1, 1, 1]))
