"""
T->O(nm) and S->min(m, n)
where m and n are lengths of both string
"""
def levenshteinDistance(str1, str2):

    rows = len(str1)+1
    cols = len(str2)+1

    dp = [[0 for _ in range(cols)] for _ in range(rows)]

    #Setting up base case which is adding each character of string in empty string
    for i in range(1, rows):
        dp[i][0] = i

    for j in range(1, cols):
        dp[0][j] = j

    for i in range(1, rows):
        for j in range(1, cols):
            
            #If chars are equal no need for edits just take diagonal value
            #otherwise take min from up, left, diagonal plus one
            if str1[i-1] == str2[j-1]:
                dp[i][j] = dp[i-1][j-1]
            else:
                dp[i][j] = min(dp[i-1][j-1], dp[i-1][j], dp[i][j-1])+1
    print(dp)
    return dp[len(str1)][len(str2)]
