class Solution(object):
    def numSpecial(self, matrix):
        m = len(matrix)
        n = len(matrix[0])
        
        c=0

        def checkCol(j):
            s = 0
            for i in range(m):
                s+=matrix[i][j]
            if s==1:
                return True
            return False

        def checkRow(i):
            s = sum(matrix[i])
            if s==1:
                return True
            return False

        for i in range(m):
            for j in range(n):
                if matrix[i][j]==1 and checkCol(j) and checkRow(i):
                    c+=1
        return c
