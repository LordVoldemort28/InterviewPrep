#Adaption of question magic potion

def repeatString(string, i, j, k):
    return string[i:(j+1)] == string[(j+1):(k+1)]

def minimalSteps(string):
    n = len(string)
    dp = [0] * n
    dp[0] = 1
    
    for i in range(1, n):
        if i%2 == 1 and repeatString(string, 0, i//2, i):
            dp[i] =  dp[i//2] + 1
        else:
            dp[i] = dp[i-1] + 1
    
    return dp[-1]

print(minimalSteps("ABABCABABCE") == 6)
print(minimalSteps("ABCDABCE") == 8)
print(minimalSteps("ABCABCE") == 5)
print(minimalSteps("AAA") == 3)
print(minimalSteps("AAAA") == 3)
print(minimalSteps("BBB") == 3)
print(minimalSteps("AAAAAA") == 4)
