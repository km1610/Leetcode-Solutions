class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        count = 0
        left_sum, right_sum = 0,sum(nums)
        
        for i in range(len(nums)-1):
            left_sum += nums[i]
            right_sum -= nums[i]

            if left_sum >= right_sum:
                count += 1
        
        return count
