class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        def get_xor_subset(i, xor):
            if i<len(nums):
                return get_xor_subset(i+1,xor) + get_xor_subset(i+1,nums[i]^xor)
            return xor
        return get_xor_subset(0,0)        
