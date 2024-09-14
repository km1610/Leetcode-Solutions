class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        maximum = max(nums)

        length = 1
    
        l = 1

        for i in range(1,len(nums)):
            if nums[i] & nums[i-1] == maximum:
                l+=1
            else:
                length = max(l,length)
                l = 1
        length = max(l,length)
        return length
