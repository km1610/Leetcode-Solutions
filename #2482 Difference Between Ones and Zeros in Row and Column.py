class Solution(object):
    def onesMinusZeros(self, grid):
        m = len(grid)
        n = len(grid[0])
        diff_matrix = []

        rows = {}
        cols = {}

        def countCol(j):
            one = 0
            for x in range(0,m):
                if grid[x][j]==1:
                    one+=1
            return one
        
        def countRow(i):
            one = grid[i].count(1)
            return one

        for i in range(m):
            rows[i] = countRow(i)


        for i in range(n):
            cols[i] = countCol(i)

        for i in range(0,m):
            row = []
            for j in range(0,n):
                onesRow, zerosRow = rows[i], (n-rows[i])
                onesCol, zerosCol = cols[j], (m-cols[j])

                row.append(onesRow + onesCol - zerosRow - zerosCol)
            diff_matrix.append(row)

        return diff_matrix
