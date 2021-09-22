class Solution:
    def rotate(self, matrix):

        n = len(matrix)

        #Transpose
        for i in range(n):
            for j in range(i, n):
                matrix[j][i], matrix[i][j] = matrix[i][j], matrix[j][i]

        #Flip
        for i in range(n):
            for j in range(n // 2):
                matrix[i][j], matrix[i][-j-1] = matrix[i][-j-1], matrix[i][j]

        return matrix


tool = Solution()
print(tool.rotate([[5, 1, 9, 11], [2, 4, 8, 10],
        [13, 3, 6, 7], [15, 14, 12, 16]]))
