class Solution(object):
    def transpose(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """

        r = len(matrix)
        c = len(matrix[0])

        transpose = [[0 for i in range(r)] for j in range(c)]

        for i in range(c):
            for j in range(r):
                transpose[i][j] = matrix[j][i]

        return transpose
