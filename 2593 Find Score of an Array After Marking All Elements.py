from heapq import *
class Solution:
    def findScore(self, nums: List[int]) -> int:
        score = 0
        heap = []
        heapify(heap)

        marked = set()

        for i in range(len(nums)):
            heappush(heap, (nums[i], i))
        
        while heap:
            e,i = heappop(heap)
            if i not in marked:
                score += e
                marked.add(i)
                marked.add(i-1)
                marked.add(i+1)

        return score
