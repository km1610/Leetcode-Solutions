class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        f = {}
        res = []
        for i in nums1:
            f[i] = 1
        
        for i in nums2:
            if i in f and f[i]==1:
                res.append(i)
                f[i] = 0

        return res
