from heapq import *
class Solution:
    def deleteGreatestValue(self, grid: List[List[int]]) -> int:
        m,n = len(grid),len(grid[0])
        rows = [[] for i in range(m)]
        for i in range(m):
            heapify(rows[i])
        for i in range(m):
            for j in range(n):
                heappush(rows[i],grid[i][j])
        sum = 0
        for i in range(n):
            maxi = -float('inf')
            for i in range(m):
                maxi = max(maxi, heappop(rows[i]))
            sum += maxi
        return sum
