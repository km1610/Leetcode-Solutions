class Solution:
    def xorAllNums(self, nums1: List[int], nums2: List[int]) -> int:
        xor = 0

        if len(nums1)%2:
            for i in nums2:
                xor = xor ^ i
                
        if len(nums2)%2:
            for i in nums1:
                xor = xor ^ i  
        
        return xor
