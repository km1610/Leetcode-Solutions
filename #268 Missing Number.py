class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n=len(nums)+1
        s = ((n*(n+1))//2)-n
        for i in range(0,n-1):
            s-=nums[i]
        return s
