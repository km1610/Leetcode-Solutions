class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort()
        s = sum(nums)
        while nums and nums[-1]>=s-nums[-1]:
            s-=nums.pop()
        if len(nums)<3:
            return -1
        return sum(nums)
