class Solution:
    def canSortArray(self, nums: List[int]) -> bool:
        def set_bits(num):
            bits = 0
            while num:
                if num%2:
                    bits += 1
                num = num >> 1
            return bits

        n = len(nums)
        for i in range(n):
            for j in range(n-1):
                if nums[j]>nums[j+1]:
                    if set_bits(nums[j]) == set_bits(nums[j+1]):
                        nums[j],nums[j+1] = nums[j+1], nums[j]
                    else:
                        return False
        return True
