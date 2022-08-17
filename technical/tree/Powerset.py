#Sliding window
def powerset(arr):
    result = []

    def dfs(i, set=[]):

        if i >= len(arr):
            result.append(set)

        else:
            #Include new number
            dfs((i+1), set+[arr[i]])

            #Don't include
            dfs((i+1), set)

    dfs(0)

    return result

print(powerset('xyz'))
