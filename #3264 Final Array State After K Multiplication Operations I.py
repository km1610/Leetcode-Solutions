import heapq
class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        heap = []
        heapq.heapify(heap)
        for i in range(len(nums)):
            heapq.heappush(heap,(nums[i],i))
        for i in range(k):
            x = heapq.heappop(heap)
            nums[x[1]] = x[0]*multiplier
            heapq.heappush(heap,(x[0]*multiplier,x[1]))
        return nums
