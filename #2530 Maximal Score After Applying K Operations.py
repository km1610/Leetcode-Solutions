from heapq import *
import math
class Solution:
    def maxKelements(self, nums: List[int], k: int) -> int:
        for i in range(len(nums)):
            nums[i] *= -1
        heapify(nums)
        score = 0
        while k:
            e = abs(heappop(nums))
            score += e
            e = math.ceil(e/3)
            heappush(nums,-e)
            k-=1
        return score
