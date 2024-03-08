class Solution:
    def diagonalSort(self, matrix: List[List[int]]) -> List[List[int]]:

        n,m = len(matrix),len(matrix[0])

        # Starting from Left

        for x in range(1,n):
            i,j = x,0
            cells = []

            while i<n and j<m:
                cells.append(matrix[i][j])
                i+=1
                j+=1
            cells.sort()

            ind = 0

            i,j = x,0
            while i<n and j<m:
                matrix[i][j] = cells[ind]
                ind+=1
                i+=1
                j+=1

        # Starting from Top

        for y in range(m):
            i,j = 0,y
            cells = []

            while i<n and j<m:
                cells.append(matrix[i][j])
                i+=1
                j+=1
            cells.sort()

            ind = 0

            i,j = 0,y
            while i<n and j<m:
                matrix[i][j] = cells[ind]
                ind+=1
                i+=1
                j+=1
        return matrix        
