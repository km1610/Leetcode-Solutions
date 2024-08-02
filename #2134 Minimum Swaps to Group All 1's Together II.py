class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        k = nums.count(1)
        max_count = s = sum(nums[:k])
        for i in range(k,len(nums)+k):
            s += nums[i%len(nums)]
            s -= nums[(i-k+len(nums))%len(nums)]
            max_count = max(s,max_count)
        return k-max_count
