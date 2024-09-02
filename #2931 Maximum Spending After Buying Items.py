from heapq import *
class Solution:
    def maxSpending(self, values: List[List[int]]) -> int:
        heap = []
        heapify(heap)
        m,n = len(values), len(values[0])
        for i in range(m):
            heappush(heap,(values[i][n-1],i,n-1))
        d = 0
        cost = 0
        while d!=m*n:
            d+=1
            item = heappop(heap)
            cost += item[0]*d
            if item[2]>0:
                heappush(heap,(values[item[1]][item[2]-1],item[1],item[2]-1))
        return cost
