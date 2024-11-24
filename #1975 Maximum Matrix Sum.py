class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        nonPositive = 0

        m, n = len(matrix), len(matrix[0])

        minAbsPositive = float('inf')
        matrixSum = 0

        for i in range(m):
            for j in range(n):
                matrixSum += abs(matrix[i][j])
                if matrix[i][j]<=0:
                    nonPositive+=1
                minAbsPositive = min(minAbsPositive, abs(matrix[i][j]))

        if nonPositive%2==0:
            return matrixSum
        else:
            return matrixSum - (2*minAbsPositive)
