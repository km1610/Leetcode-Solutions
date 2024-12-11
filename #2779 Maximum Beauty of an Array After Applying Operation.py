class Solution:
    def maximumBeauty(self, nums: List[int], k: int) -> int:

        if len(nums) == 1:
            return 1

        if min(nums) + k >= max(nums):
            return len(nums)

        nums.sort()

        def overlap(int1, int2):
            s1, e1 = int1
            s2, e2 = int2

            if s1<=s2 and e1<=e2 and e1>=s2:
                return True
            return False

        def intersect_interval(int1, int2):
            s1, e1 = int1
            s2, e2 = int2

            return [s2,e1]
        
        def sub_interval(int1,int2,int3):
            s1, e1 = int1
            s2, e2 = int2
            s3, e3 = int3
            if s1==s2:
                return int3

            return [s3, e2]

        intervals = []
        for i in nums:
            intervals.append([i-k,i+k])
        
        l, r = 0, 0
        curr = intervals[0]
        max_len = 0

        while r<len(intervals):
            if overlap(intervals[l], intervals[r]):
                curr = intersect_interval(intervals[l], intervals[r])
                max_len = max(max_len, r-l+1)
                r += 1
            else:
                curr = sub_interval(intervals[l], intervals[l+1], curr)
                l += 1
        
        return max_len
