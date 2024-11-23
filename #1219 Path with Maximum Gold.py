class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        containsGold = []

        m, n = len(grid), len(grid[0])
        for i in range(m):
            for j in range(n):
                if grid[i][j]:
                    containsGold.append([i,j])
        
        def Traverse(i, j, visited, gold):
            if i==-1 or i==m or j==-1 or j==n:
                return gold
            if grid[i][j] == 0:
                return gold
            if (i,j) in visited:
                return gold

            return max(Traverse(i+1,j,visited.union({(i,j)}),gold + grid[i][j]), Traverse(i,j-1,visited.union({(i,j)}),gold + grid[i][j]), Traverse(i-1,j,visited.union({(i,j)}),gold + grid[i][j]), Traverse(i,j+1,visited.union({(i,j)}),gold + grid[i][j]))

        maxGold = 0

        for cells in containsGold:
            x,y = cells[0],cells[1]
            
            maxGold = max(maxGold, Traverse(x,y,set(),0))

        return maxGold
