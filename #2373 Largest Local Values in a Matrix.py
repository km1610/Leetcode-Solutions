class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        n = len(grid)
        matrix = [[0 for i in range(n-2)] for j in range(n-2)]
        for i in range(n):
            if i-1<0 or i+1>=n:
                continue
            for j in range(n):
                if j-1<0 or j+1>=n:
                    continue
                matrix[i-1][j-1] = max(grid[i-1][j-1],grid[i-1][j],grid[i-1][j+1],grid[i][j-1],grid[i][j],grid[i][j+1],grid[i+1][j-1],grid[i+1][j],grid[i+1][j+1])
        return matrix
